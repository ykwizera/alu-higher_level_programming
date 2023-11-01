#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')
while True:
    char = input("Enter a character: ")
    if islower(char):
        print("True")
    else:
        print("False")
