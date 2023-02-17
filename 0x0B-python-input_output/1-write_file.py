#!/usr/bin/python3
"""
Module containing function to write data to file
using utf-8
"""


def write_file(filename="", text=""):
    """
    Fucntion to write text to file
    Args:
        filename: Filename
        text: text to write to file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        wc = f.write(text)
    return(wc)

