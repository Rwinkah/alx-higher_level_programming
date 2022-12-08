#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == []:
        return matrix
    list_ans = []
    for row in matrix:
        list_temp = list(map(lambda x: x ** 2, row))
        list_ans.append(list_temp)
    return list_ans
