#!/usr/bin/python3
"""
Defines a Square class that validates size and computes area.
"""


class Square:
    """
    Represents a square with a private validated size.
    """

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size (int): size of the square (default: 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size
