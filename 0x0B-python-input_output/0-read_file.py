#!/usr/bin/python3

"""read_file module"""


def read_file(filename=""):
    '''
    Reads a text file using UTF-8 encoding and prints its contents to stdout.
    Uses 'with' statement for resource management.
    '''

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
