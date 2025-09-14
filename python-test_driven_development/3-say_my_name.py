#!/usr/bin/python3

"""
This module provides a function that prints a full name,
constructed from a first and an optional last name.
"""


def say_my_name(first_name="", last_name=""):
    """
    Prints "My name is <first_name> <last_name>"

    Args:
        first_name (str): le prénom
        last_name (str): le nom de famille (optionnel)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = (first_name + " " + last_name).strip()
    print("My name is " + full_name)
