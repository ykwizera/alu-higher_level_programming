#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result = sorted(a_dictionary.keys())
    for key in result:
        print(f"{key}: {a_dictionary[key]}")
    return result
