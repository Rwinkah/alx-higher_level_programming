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
    if (type(a) != int and type(a) != float or b is None):
        raise TypeError("a must be an integer")

    if (type(b) != int and type(b) != float or b is None):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
