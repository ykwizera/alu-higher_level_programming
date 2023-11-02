#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    num_args = len(argv)
    a = 's' if num_args != 1 else ''
    b = ':' if num_args != 0 else '.'
    print("{} argument{}{}".format(num_args, a, b))
    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
