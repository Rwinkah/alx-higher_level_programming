#!/usr/bin/python3
""" This module returns the dictionary description with simple
    data structure for json serialization of an object.
"""


def class_to_json(obj):
    """ Return dictionary description """
    return obj.__dict__
