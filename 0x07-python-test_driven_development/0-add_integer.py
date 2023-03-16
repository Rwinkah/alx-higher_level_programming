#!/usr/bin/python3
"""
    function to add two ints
    Args:
        a: first number
        b: second number
    Return:
        int
"""


def add_integer(a, b=98):
    """
        function to add two numbers
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
