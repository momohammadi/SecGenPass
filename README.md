# SecGenPass a Powerful password generator

This Python script generates random passwords based on specified criteria such as length, the number of special characters, and inclusion of specific special characters.
## Idea behind this script
As individuals engaged in development environments and infrastructures daily, we often encounter the need to set up and use multiple passwords. Until now, I've utilized various methods to create secure passwords, including online sites like passwordgenerator.net or tools like KeePass, among others. However, all these methods share common issues: they are time-consuming and unsuitable for automation. Due to these reasons and others, including the lack of reliability in online password generation sites, I developed this script for myself and decided to share it with you.

This script is straightforward, fast, and also suitable for use in automation environments.
## Usage
This script can be seamlessly integrated into your bash alias, ensuring convenient and swift access for daily usage. Additionally, it's adaptable for embedding within your code, providing a reliable method to generate random passwords within any script or program.

Feel empowered to adjust the command-line arguments or tailor the script to suit your specific requirements!


### Docker Usage
Generate passwords using a Docker image based on a web server and retrieve them via curl, customizing the output with query parameters.

1. Run Docker Container with a custom port

    ```bash
    hostPort=8080
    docker run -d -p $hostPort:80 momohammadi/secgenpass --name secgenpass
    ```
2. Get a password with the following command:

    this will generate password with default arguments

    ```bash
    # default setting
    curl localhost:$hostPort
    ```

    This will generate 5 passwords with lengths of 20 characters each, containing between 3 to 5 special characters.

    ```bash
    # customize output password 
    curl -X Get localhost:$hostPort?n=5&s=3&m=5&l=20
    ```

### Direct Usage
##### Prerequisites
- Python 3.x

1. Clone the repository:

    ```bash
    git clone https://github.com/momohammadi/SecGenPass.git
    ```

2. Navigate to the directory:

    ```bash
    cd SecGenPass
    ```

3. Run the script with the following command-line arguments:

    ```bash
    # default setting
    python SecGenPass.py
    
    # customize output password 
    python SecGenPass.py [-h] [-i INCLUDE] [-n NUMBER] [-s MIN] [-m MAX] [-l LENGTH]
    ```

    #### Command-line arguments:
    - `-h, --help`: Showing Help message
    - `-i, --include`: Include these special characters in the password (default: `?)$!=+`)
    - `-n, --number`: Number of generated passwords (default: `1`)
    - `-s, --min`: Minimum number of special characters in the generated password (default: `4`)
    - `-m, --max`: Maximum number of special characters in the generated password (default: `4`)
    - `-l, --length`: Length of the generated passwords (default: `19`)

    **Example:**

    ```bash
    python SecGenPass.py -n 5 -s 3 -m 5 -l 20
    ```

    This will generate 5 passwords with lengths of 20 characters each, containing between 3 to 5 special characters.

### Functionality

The script uses the following functions:

- `passgen(length, min_special_chars, max_special_chars, special_chars)`: Generates a password with the specified length and number of special characters.
- `generate_passwords(num_passwords)`: Generates a list of passwords based on the provided number.

## How it Works

The script utilizes the `random` and `string` modules in Python to generate random passwords based on the provided criteria. It employs a character set comprising lowercase and uppercase letters, digits, and user-defined special characters. The generated passwords meet the specified length and criteria regarding the number of special characters included.

