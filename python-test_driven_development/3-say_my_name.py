#!/usr/bin/python3
"""
Module that prints a full name in the format:
My name is <first name> <last name>.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the full name.

    Args:
        first_name (str): the first name
        last_name (str): the last name (optional)

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
