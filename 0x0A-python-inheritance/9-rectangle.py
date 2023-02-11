#!/usr/bin/python3
""" class Recangle inheriting from BaseGeometry """
BaseGeometry = __import__(7-base_geometry.py).BaseGeometry



class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validation("width", width)
        self.__width = width
        self.integer_validation("height", height)
        self.__height = height

    def area(self):
        """ method to return the area of the rectangle """
        return (self.__width * self.__height)


    def print(self):
        """ Print method printing string representation of class """
        print(self.str)


    def __str__(self):
        """ String representation of class """
        return ("[Rectangle] {}/{}".format(self.__width, self.height))
