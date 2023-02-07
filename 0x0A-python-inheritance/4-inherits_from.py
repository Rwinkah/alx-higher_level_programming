#!/usr/bin/python3
""" Check if Obj  inherits directly or indirectly from class"""


def inherits_from(obj, a_class):
    """function to perform the check
    Args:
        obj (any): The object to check
        a_class: any class
    Return:
        Boolean
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
