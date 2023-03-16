#!/usr/bin/python3
""" Module to print a square using # """


def print_square(size):
    """ Print a square when requirements are met """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError('size must be an integer')
    if size < 0 and not isinstance(size, float):
        raise ValueError('size must be >= 0')
    if (isinstance(size, float) and size < 0):
        raise TypeError('size must be an integer')

    size = int(size) 
    for i in range(size):
        for j in range(size):
            print('#', end="")
