#!/usr/bin/python3
"""
Python Module Defining a function to read data from a file and
print it to stdout.
"""


def read_file(filename=""):
    """ Function to read data from a file and print to stdout """
    with open(filename, encoding="utf-8") as f:
        for line in f: 
            print(line, end="")
    return 0
