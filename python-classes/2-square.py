#!/usr/bin/python3
"""
This module defines a Square class that validates size.
"""


class Square:
    """
    Represents a square with validated private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize the square with an optional size.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
