#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    square all values in a matrix
    Args:
        matrix = input matrix
    Return:
        new_matrix
    """
    return(list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
