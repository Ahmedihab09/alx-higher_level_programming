#!/usr/bin/python3

'''Write function module'''


def write_file(filename="", text=""):
    '''
    Writes a given string to a text file with UTF-8 encoding.
    The function creates the file if it doesn't exist, or overwrites it if it does.
    It returns the number of characters written.
    '''
    with open(filename, "w", encoding="utf-8") as file:
        char_count = file.write(text)
        return char_count
