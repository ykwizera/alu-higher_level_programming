#!/usr/bin/python3
# 3-square.py


"""
This is my module
"""


class Square:
    """
    This is my class
    """
    def __init__(self, size=0):
        """
        This is y init module
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        calculatung the area using size
        """
        return self.__size * self.__size
