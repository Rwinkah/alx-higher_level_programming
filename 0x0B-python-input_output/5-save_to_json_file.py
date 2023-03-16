#!/usr/bin/python3
""" write an object into a file using json rep of the obj """
import json


def save_to_json_file(my_obj, filename):
    """ write json rep of obj into filename """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
