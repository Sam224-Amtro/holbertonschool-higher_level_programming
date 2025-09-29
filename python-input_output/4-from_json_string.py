#!/usr/bin/python3
"""Module pour JSON String"""
import json


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en une structure de données Python.

    Args:
        ma_chaine (str) : Une chaîne au format JSON.

    Returns:
        object : L'objet Python représenté par la chaîne JSON.
    """
    return json.loads(my_str)
