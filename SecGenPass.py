import random
import string
import argparse

if __name__ == "__main__":
    # Create an argument parser to handle command-line arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--include", help="Include these special characters in the password", default='?)$!=+')
    argParser.add_argument("-n", "--number", type=int, help="Number of generated passwords", default=1)
    argParser.add_argument("-s", "--min", type=int, help="Minimum number of special characters in the generated password", default=4)
    argParser.add_argument("-m", "--max", type=int, help="Maximum number of special characters in the generated password", default=4)
    argParser.add_argument("-l", "--length", type=int, help="Length of the generated passwords", default=19)
    args = argParser.parse_args()

    # Extract values from command-line arguments
    special_chars = args.include
    num_passwords = args.number
    min_special_chars = args.min
    max_special_chars = args.max
    length = args.length

def passgen(length: int, min_special_chars: int, max_special_chars: int, special_chars: str) -> str:
    # Define the character set for generating passwords
    all_chars = string.ascii_letters + string.digits + special_chars

    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        special_chars_count = sum(1 for c in password if c in special_chars)
        if (
            not password[0] in special_chars and
            not password[-1] in special_chars and            
            not password[0].isdigit() and
            not password[-1].isdigit() and
            min_special_chars <= special_chars_count <= max_special_chars
        ):
            return password

def generate_passwords(num_passwords: int) -> list:
    passwords = []

    while num_passwords > 0:
        # Check if the maximum special characters value is greater than or equal to the minimum value
        if max_special_chars >= min_special_chars:
            password = passgen(length, min_special_chars, max_special_chars, special_chars)
            passwords.append(password)
            num_passwords -= 1
        else:
            # Handle the case where max_special_chars < min_special_chars to avoid infinite loop
            print(f"Error: The maximum number of special characters ({max_special_chars}) is less than the minimum ({min_special_chars})")
            break
    return passwords

# Generate and print passwords
passwords = generate_passwords(num_passwords)
for password in passwords:
    print(password)