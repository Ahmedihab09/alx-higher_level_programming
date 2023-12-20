#!/usr/bin/python3

'''Sqaure Class'''


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): Private instance attribute
        representing the size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
