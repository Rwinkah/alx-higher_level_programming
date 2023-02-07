#!/usr/bin/python3
""" Module creating an empty class """


class BaseGeometry():
    """An empty class named BaseGeometry"""
    def __init__(self):
        pass

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
