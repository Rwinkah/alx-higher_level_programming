#!/usr/bin/python3
def complex_delete(inp_dict, val):
    remv = []
    inp_copy = inp_dict
    for key, value in inp_copy.items():
        if val == value:
            remv.append(key)
    if len(remv) == 0:
        return inp_copy
    for i in remv:
        inp_copy.pop(i)
    return inp_copy
