#!/usr/bin/python3
"""Class Square inheriting from class Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class from Rectangle
    Args:
        size(int): size of the square
    """

    def __init__(self, size):
        """Initialize Square class."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """String implementation of class."""
        return ("[square] {}/{}".format(self.__size, self.__size)
