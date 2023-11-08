#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result = sorted(a_dictionary.items())
    sort = {}
    for key,value in result:
        sort[key] = value
    return sort
