#!/usr/bin/python3
""" This module adds all args to python list and then saves them to a file """Z


import sys

load_js = __import__('6-load_from_json_file').load_from_json_file
save_js = __import__('5-dave_to_json_file').save_to_json_file


try:
    items = load_js('add_item.json')
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_js(items, 'add_item.json')
