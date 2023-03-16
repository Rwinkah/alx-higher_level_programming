#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    return weighted average from a list of tuples
    Args:
        my_list: input list
    Return:
        weighted average: float
    """
    if len(my_list) == 0 or my_list is None:
        return 0

    we_average = 0
    we_div = 0

    for i in my_list:
        we_average += i[0] * i[1]
        we_div += i[1]

    return we_average / we_div
