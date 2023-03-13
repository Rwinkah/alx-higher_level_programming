#!/usr/bin/python3
""" A class student """


class Student:
    """ Class representation of a student """

    def __init__(self, first_name, last_name, age):
        """ Initialize a student object with first, last name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return a dict representation of student """
        return self.__dict__
