#!/usr/bin/python3

"""
Module for say_my_name function.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        print("My name is {:s}".format(first_name))
