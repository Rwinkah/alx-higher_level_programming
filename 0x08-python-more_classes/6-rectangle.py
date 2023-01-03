#!/usr/bin/python3

""" Module defining a class Rectangle """


class Rectangle:
    """ Proper Rectangle class """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """ get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the height of the rectangle """
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """ gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ set the width of the rectangle """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def area(self):
        """ Returns the are of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Print rectangle using to string method """
        if self.__width == 0 or self.__height == 0:
            return ""
        disp = []
        for i in range(self.__height):
            for width in range(self.__width):
                disp.append("#")
            if i != self.height - 1:
                disp.append("\n")

        return "".join(disp)

    def __repr__(self):
        """ String representation of Rectangle Class """
        rect = "Rectangle(" + str(self.__width) + ", " + str(self.__height)
        rect += ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
