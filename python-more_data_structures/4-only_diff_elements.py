#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elts = set()
    for item in set_1:
        if item not in set_2:
            diff_elts.add(item)
    for items in set_2:
        if items not in set_1:
            diff_elts.add(items)
    return diff_elts
