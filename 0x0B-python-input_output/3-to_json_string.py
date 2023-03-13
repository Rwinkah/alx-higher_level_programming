#!/usr/bin/python3
"""
Return the json representation of an object
Args:
    my_obj: input object
"""

import json

def to_json_string(my_obj):
    """ Return json representation of an object """

    return json.dumps(my_obj)
