#!/usr/bin/python3
"""Defining a function to delete a member of a dictionary using a key."""


def simple_delete(a_dictionary, key=""):
    """
    simple delete from dictionary
    Args:
        a_dictionary(dict): dictionary to delete from
        key(string): key to delete from dict
    """
    if key not in a_dictionary:
        return a_dictionary

    a_dictionary.pop(key)
    return a_dictionary
