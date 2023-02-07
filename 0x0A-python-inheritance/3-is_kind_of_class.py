#!/usr/bin/python3
""" Check if Obj is an instance of a class """


def is_same_class(obj, a_class):
    """function to perform the check
    Args:
        obj (any): The object to check
        a_class: any class
    Return:
        Boolean
    """
    return (isinstance(obj, a_class))
