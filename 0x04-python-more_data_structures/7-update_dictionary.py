#!/usr/bin/python3
"""Define function to update dictionary values"""


def update_dictionary(a_dictionary, key, value):
    """
    Updating dictionary values
    Args:
        a_dictionary(dict): dictionary to update
        key(string): Key to add or update in dictionary
        value(any): value to add with key
    """
    a_dictionary[key] = value
    return (a_dictionary)
