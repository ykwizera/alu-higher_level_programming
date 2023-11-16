#!/usr/bin/python3
# 4-square.py


"""
This is my module
"""


class Square:
    """
    This is my square class
    """
    def get_size(self):
        """
        get function
        """
        return self.__size
    def set_size(self, size):
        """
        set module
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def size(self):
        """
        size module
        """
        return self.get_size()
    def size(self, value):
        """
        size module 2
        """
        self.set_size(value)
    def __init__(self, size=0):
        """
        initialising size
        """
        self.set_size(size)
    def area(self):
        """
        Calculating the area using size
        """
        return self.__size * self.__size
