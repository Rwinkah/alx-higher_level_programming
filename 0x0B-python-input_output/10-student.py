#!/usr/bin/python3
""" Update on class student """


class Student:
    """ Class studnet """

    def __init__(self, first_name, last_name, age):
        """ init function for student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dict representation of required attributes"""
        if isinstance(attrs, list) and all(type(i) == str for i in attr):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        else:
            return self.__dict__
