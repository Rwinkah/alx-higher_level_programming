#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    new_list = my_list[:]
    if idx < len(new_list):
        new_list[idx] = element
