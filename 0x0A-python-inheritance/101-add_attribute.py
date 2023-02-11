#!/usr/bin/python3
"""Function to set the value of the attribute of an object."""


def add_attribute(object, attrname, value):
    """
    function to add an attribute to an object
    Args:
        object: An object of any class
        attrname: Attribute to add to the class
        value: Value of new attribute
    """

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attrname, value)
