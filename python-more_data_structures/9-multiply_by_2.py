#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = {}
    for key, value in a_dictionary.items():
        a[key] = value*2
    return a
