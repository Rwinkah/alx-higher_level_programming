#!/usr/bin/python3
""" Module to create a base class """

class Base():
    """ empty class base """
    __nb_objects = 0

    def __init__(self, id=None):
        if (id):
           self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects


