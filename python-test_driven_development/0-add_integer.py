#!/usr/bin/python3
"""
    Add two integers or floats together
    and return the result as an integer.
"""


def add_integer(a, b=98):

    """_summary_

    Args:
        a (_type_): variable
        b (int, optional): variable, defaults to 98.

    Raises:
        TypeError: a doit être un entier
        TypeError: b doit être un entier

    Returns:
        _type_: retourne un int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
