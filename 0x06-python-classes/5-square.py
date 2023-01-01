#!/usr/bin/python3

""" Square class with private property implementing getters and setters """


class Square:
    """ A class to show the getter encapsulation of private attributes"""

    def __init__(self, sizee=0):
        self.__size = sizee

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, sizee):
        if type(sizee) != int:
            raise TypeError("size must be an integer")
        elif sizee < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = sizee

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        area = self.__size
        if area == 0:
            print("")
            return

        for length in range(area):
            for breadth in range(area):
                print('#', end='')
            print("")
