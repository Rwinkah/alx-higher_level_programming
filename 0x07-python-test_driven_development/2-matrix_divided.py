#!/usr/bin/python3
"""
    Function to perform scalar division on a matrix
    Args:
        matrix: list of list of integers
        div: number to divide by
    Return:
        new matrix
"""


def matrix_divided(matrix, div):
    """
    function to perform scalar division on a matrix
    """

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError("matrix musr be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for num in lst:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    lenlist = len(matrix[0])
    for lst in matrix:
        if len(lst) != lenlist:
            raise TypeError("Each row of the matrix must have the same size")

    return([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
