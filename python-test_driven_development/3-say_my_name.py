#!/usr/bin/python3
"""
Prints the full name in the format: My name is <first name> <last name>.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format: My name is <first name> <last name>.

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Pas de strip() -> garde l’espace final si last_name est vide
    print(f"My name is {first_name} {last_name}")
