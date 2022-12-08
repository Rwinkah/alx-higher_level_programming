#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_ans = set()
    for elm in set_1:
        if elm not in set_2:
            set_ans.add(elm)
    for elm in set_2:
        if elm not in set_1:
            set_ans.add(elm)
    return set_ans
