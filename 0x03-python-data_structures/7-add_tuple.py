#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_b = list(tuple_b)
    while len(list_b) < 2:
        list_b.append(0)
    tuple_b = list(list_b)
    list_a = list(tuple_a)
    while len(list_a) < 2:
        list_a.append(0)
    tuple_a = list(list_a)
    zip_list = list(zip(tuple_a, tuple_b))
    i = 0
    list_ans = []
    for i in range(2):
        list_ans.append(sum(zip_list[i]))

    return (tuple(list_ans))
