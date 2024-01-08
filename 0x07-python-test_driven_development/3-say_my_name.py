#!/usr/bin/python3

"""Module that prints My name is <first name> <last name>."""


def say_my_name(first_name, last_name=""):
    """
    Prints a full name.

    Args:
    first_name (str): The first name.
    last_name (str): The last name. Defaults to an empty string.

    Raises:
    TypeError: If either first_name or last_name is not a string.

    Returns:
    None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
