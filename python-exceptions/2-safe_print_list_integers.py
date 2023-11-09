#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        i = 0
        while True:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
            i += 1
            if printed_integers >= x:
                break
    except (IndexError, TypeError):
        pass

    print()
    return printed_integers
