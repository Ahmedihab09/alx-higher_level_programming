#!/usr/bin/python3 

"""read_file module"""


def read_file(filename=""):
    # Use 'with' statement for safe opening and closing of the file
    with open(filename, "r", encoding="utf-8") as file:
        # Read the file line by line and print to stdout
        for line in file:
            print(line, end="")
