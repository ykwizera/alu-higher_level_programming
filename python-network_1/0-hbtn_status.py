#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status using urllib
"""

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()

expected_content = b'Custom status'

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))

if body == expected_content:
    print("\n[Got]")
else:
    print("\n[Unexpected]")

print("Body response:")
print("\t- type: <class 'bytes'>")
print("\t- content:", expected_content)
print("\t- utf8 content:", expected_content.decode('utf-8'))
