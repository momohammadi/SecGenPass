#!/usr/bin/env python
import http.server
import os, signal, sys
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class CustomHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if parsed_url.path == "/":
            self.handle_root_request(query_params)
        else:
            self.send_error(404, f'File Not Found: {self.path}')

    def handle_root_request(self, query_params):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        # Get parameters from the query string
        params = {key: value[0] for key, value in query_params.items()}

        # Construct command based on provided parameters
        command = ['python', 'SecGenPass.py']
        for key, value in params.items():
            command.extend([f'-{key}', value])

        # Run SecGenPass.py with constructed command and capture the output
        output = os.popen(' '.join(command)).read()

        # Send the output as the response
        self.wfile.write(bytes(output, "utf-8"))

def currentTime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def run(server_class=http.server.HTTPServer, handler_class=CustomHandler):
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    
    # Function to handle termination signal
    def handle_exit(signum, frame):
        print(f"{currentTime()} Received termination signal. Exiting gracefully...")
        httpd.server_close()
        print(f"{currentTime()} Successfully shutdown http server")
        sys.exit(0)

    # Register SIGTERM signal handler
    signal.signal(signal.SIGTERM, handle_exit)

    try:
        print(f"{currentTime()} Starting server on port 80...")
        sys.stdout.flush()
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == '__main__':
    run()
