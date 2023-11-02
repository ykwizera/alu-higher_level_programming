#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    num_args = len(argv)
    print("{} argument{}{}".format(num_args, 's' if num_args != 1 else '', '.' if num_args == 0 else ':'))
    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
