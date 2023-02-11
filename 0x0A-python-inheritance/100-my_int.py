#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Class inheriting from int."""

    def __eq__(self, other):
        """Magic method for equality overwritten."""
        return self.real != other

    def __ne__(self, other):
        """Magic method for inequality overwritten."""
        return self.real == other 
