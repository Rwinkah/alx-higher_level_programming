#!/usr/bin/python3
""" Check if Obj is an instance of a class  that inherita directly or indirectly"""


def inherits_from(obj, a_class):
    """function to perform the check
    Args:
        obj (any): The object to check
        a_class: any class
    Return:
        Boolean
    """
    return (issubclass(obj, a_class))
