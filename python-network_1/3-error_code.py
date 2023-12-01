#!/usr/bin/python3

import sys
from urllib import request, error

def fetch_request_id(url):
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <url>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    request_id = fetch_request_id(url)

    if request_id:
        print("X-Request-Id: {}".format(request_id))
