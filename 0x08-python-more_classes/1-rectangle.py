#!/usr/bin/python3

""" Module defining a class Rectangle """


class Rectangle:
    """ Proper Rectangle class """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """ get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value 

    @property
    def width(self):
        """ gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width of the rectangle """
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value 
