#!/usr/bin/python3

def remove_char_at(str, n):
    list_str = list(str)
    if n < len(list_str) and n >= 0:
        list_str.pop(n)
    return "".join(list_str)
