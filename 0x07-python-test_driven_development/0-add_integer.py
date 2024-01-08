#!/usr/bin/python3

"""Module that adds 2 integers."""


def add_integer(a, b=98):
    """
    Function to add two numbers.

    Args:
    a (int or float): The first number to add.
    b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
    int: The sum of a and b after casting them to integers.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
