#!/usr/bin/python3
"""
    Function to print out a user name
    Args:
        First_name: User first name
        Last_name: User last name
"""


def say_my_name(first_name, last_name=""):
    """
      Print out a first and last name
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
