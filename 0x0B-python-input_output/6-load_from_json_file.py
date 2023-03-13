#!/usr/bin/python3
""" This module loads a json object from a file """
import json


def load_from_json_file(filename):
    """ load an obj from a json file """
    with open(filename) as f:
        return json.load(f)
