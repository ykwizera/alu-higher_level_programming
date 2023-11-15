#!/usr/bin/python3
# 1-square.py

"""
This is my module.
"""

class Square:
    """
    This is my Square class with a private attribute size.
    """
    def __init__(self, size):
        """
        Initializes the Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
