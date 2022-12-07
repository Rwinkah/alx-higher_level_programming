#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 1
    if matrix == [[]]:
        print("")
        return matrix
    for row in matrix:
        for cell in row:
            print('{:d}'.format(cell), end='')
            i += 1
            if i <= len(row):
                print(' ', end="")
            else:
                print("")
        i = 1
