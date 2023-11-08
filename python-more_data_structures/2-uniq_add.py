#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    result = 0
    for num in my_list:
        if num not in unique:
            result += num
            unique.add(num)
    return result
