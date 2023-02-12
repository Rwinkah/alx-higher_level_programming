#!/usr/bin/python3
"""Defines function for printing dictionary elements by sorted keys."""


def print_sorted_dictionary(a_dictionary):
    """
    Print dictionary by sorted keys
    Args:
        a_dictionary(dict): dictionary to sort
    """

    list_keys = list(a_dictionary.keys())
    list_keys.sort()

    for i in list_keys:
        print("{}: {}".format(i, a_dictionary[i]))
