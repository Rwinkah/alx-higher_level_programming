#!/usr/bin/python3
"""Module creating a class named Rectangle """

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """ Class Rectangle inheriting from class BaseGeometry"""


def __init_(self, width, height):
    """ Initialize a new Rectangle """
    self.integer_validator("width", width)
    self.__width = width
    self.integer_validator("height, height)
    self.__height = height
