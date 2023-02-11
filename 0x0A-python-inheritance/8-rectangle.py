#!/usr/bin/python3
""" Module creating an empty class """


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry named Rectangle"""

    def __init__(self, width, height):
        """ Initialiazation method of the Rectangle class """
        self.__width = width
        self.__height = height

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self):
        """ Check for valid inputs """
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be greater than 0")

        if type(self.__width) != int:
            raise TypeError(" width must be an integer")
        if self.__height <= 0:
            raise ValueError("width must be greater than 0")
