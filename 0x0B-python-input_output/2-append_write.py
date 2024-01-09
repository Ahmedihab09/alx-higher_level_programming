#!/usr/bin/python3

'''append write module'''


def append_write(filename="", text=""):
    '''
    Appends a string at the end of a text file (UTF8).
    If the file doesn’t exist, it's created.
    Returns the number of characters added.
    '''
    with open(filename, "a", encoding="utf-8") as file:
        char_count = file.write(text)
        return char_count
