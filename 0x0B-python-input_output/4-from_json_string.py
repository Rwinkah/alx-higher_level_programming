#!/usr/bin/python3
"""
Module to read data from an input json file
"""


def from_json_string(my_str):
    """Load a json object """
    return json.loads(my_str)
