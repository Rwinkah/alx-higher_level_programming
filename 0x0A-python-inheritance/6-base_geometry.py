#!/usr/bin/python3
""" Module creating an empty class """


class BaseGeometry():
    """An empty class named BaseGeometry"""
    def __init__(self):
        pass

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")
