#!/usr/bin/python3

def best_score(inp_dict):
    """
    Function to return the key of the largest value in a dictionary
    Args:
        inp_dict: input dictionary
    Return:
        key: string
    """
    if inp_dict is not None:
        return(max(inp_dict, key=inp_dict.get))
