#!/usr/bin/python3
"""Are you docuemnted ?"""


import json


def save_to_json_file(my_obj, filename):
    """Why THough"""
    with open(filename, "w+") as f:
        return json.dump(my_obj, f)
