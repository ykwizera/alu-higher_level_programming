#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        x = my_list[:]
        new_element = element
        x[idx] = new_element
        return x
    
    print("{:d}".format(my_list))
