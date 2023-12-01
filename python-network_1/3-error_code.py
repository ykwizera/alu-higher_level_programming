#!/usr/bin/python3
# Module 1: urllib.request
import urllib.request
import urllib.error
import sys
def fetch_url_content(url):
    #function
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided.
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    # Extract the URL from the command-line argument.
    url = sys.argv[1]

    # Call the fetch_url_content function with the provided URL.
    fetch_url_content(url)
