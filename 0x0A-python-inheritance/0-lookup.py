#!/usr/bin/python3
"""return the list of available attributes and methods of an object """


def lookup(obj):
    return list(obj.__dict__)