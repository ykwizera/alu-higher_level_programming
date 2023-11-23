#!/usr/bin/python3
"""Are you docuemnted ?"""


import json


def load_from_json_file(filename):
    """How far"""
    with open(filename, "r") as f:
        return json.load(f)
