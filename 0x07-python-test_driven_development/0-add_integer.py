#!/usr/bin/python3
"""  python function to add two numbers and
test the function using doctest module
"""


def add_integer(a, b=98):
    """
    function to add two numbers
        args:
            a: int / float
            b: int / float
        return:
            int
"""

    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    if a == NaN or b == NaN:
        raise TypeError('cannot convert float NaN to integer')
    return(int(a) + int(b))
