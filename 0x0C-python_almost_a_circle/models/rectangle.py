#!/usr/bin/python3
""" Module to define a rectangle """

from models.base import Base
class Rectangle(Base):
    """ Class defining a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method for rectangle """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self, value):
        """ return the value of width """
        return self.__width


    @width.setter
    def width(self, value):
        """ setter for the private variable width """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property 
    def height(self, value): 
        """ getter for height """
        return self.__height


    @height.setter
    def height(self, value):
        """ setter for the private variable height """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self, value):
        """ getter for private instance variable x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for the private instance variable x """
        if value < 0:
            raise ValueError('x must be >= 0')
        if type(value) != int:
            raise TypeError('x must be an integer')
        self.__x = value


    @property
    def y(self, value):
        """ getter for private instance variable y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for private instance variable y """
        if type(value) != int:
           raise TypeError('y must be an integer')
        if value < 0:
           raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ calculate are of the triangle """ 
        return (self.__width * self.__height)

    def display(self):
        """ print the rectangle using # """
        count = 0
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print("#", end="")
                count += 1
        return count

    def __str__(self):
        """ overriding the string method """
        clname = self.__class__.__name__
        rid = self.id
        xandy = f'{self.__x}/{self.__y}'
        wandh = f'{self.__width}/{self.__height}'
        return f'[{clname}] ({rid}) {xandy} - {wandh}'

    def update(self, *args):
        """ updating the attributes of the rectangle """
        if args is not None:
            lnt = len(args)
            self.id = args[0] if lnt > 0  else self.id
            self.__width = args[1] if lnt > 1 else self.__width
            self.__height = args[2] if lnt > 2 else self.__height
            self.__x = args[3] if lnt > 3 else self.__x
            self.__y = args[4] if lnt > 4 else self.__y
            return

        self.id = kwargs.get('id', self.id)
        self.__width = kwargs.get('width', self.__width)
        self.__height = kwargs.get('height', self.__height)
        self.__x = kwargs.get('x', self.__x)
        self.__y = kwargs.get('y', self.__y)
