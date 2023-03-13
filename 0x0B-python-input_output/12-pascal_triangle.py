#!/usr/bin/python3
""" Module returning a list representing a pascal triangle for len n """


def pascal_triangle(n):
    """ pascal_triangle function """

    triangle = [[1]]

    if n <= 0:
        return []

    while len(triangle) != n:
        tier = triangle[-1]
        temp = [1]
        for i in range(len(tier) - 1):
            temp.append(tier[i] + tier[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
