#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializing the complete Rectangle class
        Args:
            width(int):  width of rectangle
            height(int): height of rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to return the area of the rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """String representation of class."""
        name = self.__class__.__name__
        return ("[{}] {}/{}".format(name, self.__width, self.__height))
