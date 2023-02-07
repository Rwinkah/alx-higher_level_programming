#!/usr/bin/python3
""" Class MyList with method print_sorted """


class MyList(list):
    """ Class definition """

    def print_sorted(self):
        """Print method to sort the list"""
        print(sorted(self))
