#!/usr/bin/python3

"""Module that prints a text with 2 new lines after each of these characters:
    ., ? and :."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Arguments:
    text (str): The text to be processed and printed.

    Raises:
    TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1

