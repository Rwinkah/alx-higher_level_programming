#!/usr/bin/python3

""" Module defining a class square with validation for size """


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ Initialization method for the class
        Args:
                size(int): Size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
