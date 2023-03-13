#!/usr/bin/python3
""" Update on class student """


class Student:
    """ Class for student """
    def __init__(self, first_name, last_name, age):
        """ init function for student """
        self.fname = first_name
        self.lname = last_name
        self.age = age

    def to_json(self, att=None):
        """ return dict representation of required attributes """

        if (isinstance(att, list) and all(type(i) == str for i in att)):
            return {i: getattr(self, i) for i in att if hasattr(self, i)}
        else:
            return self.__dict__

    def reload_from_json(self, json_dict):
        """ load data for attrs from student """
        for attrib, value in json_dict.items():
            setattr(self, attrib, value)
