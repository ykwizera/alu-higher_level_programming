#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request, displays
the value of the X-Request-Id variable found in the header,
and handles HTTP errors.
"""


import sys
from urllib import request, error

def fetch_request_id(url):
    """ function"""
    try:
        with request.urlopen(url) as response:
            request_id = response.headers.get('X-Request-Id')
            if request_id:
                return request_id
            else:
                print("Error: No X-Request-Id header found")
                return None
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <url>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    request_id = fetch_request_id(url)

    if request_id:
        print("X-Request-Id: {}".format(request_id))

if __name__ == "__main__":
    main()
