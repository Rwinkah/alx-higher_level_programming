#!/usr/bin/python3

def multiply_by_2(inp_dict):
    """
    Function returns a new dictionary with all integer values multiplied by 2
    Args:
        a_dictionary: input dictionary
    Return:
        new_dictionary
    """

    list_keys = [i for i in inp_dic.keys()]
    new_dict = inp_dict.copy()
    for i in list_keys:
       new_dict[i] *= 2
    return new_dict
