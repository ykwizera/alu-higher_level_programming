#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    if chr(char_code) == 'e' or chr(char_code) == 'q':
        continue
    print("{}".format(chr(char_code)), end='')
