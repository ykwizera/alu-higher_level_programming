#!/usr/bin/python3
def no_c(my_string):
    x = ""
    for char in my_string:
        if char not in 'cC':
            x += char
    return x
