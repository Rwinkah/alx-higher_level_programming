#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0
    set_ans = set(my_list)
    return sum(set_ans)
