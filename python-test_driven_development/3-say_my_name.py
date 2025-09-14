#!/usr/bin/python3
"""
    prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): string first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: Si le first_name n'est pas une string
        TypeError: Si le last_name n'est pas une string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
