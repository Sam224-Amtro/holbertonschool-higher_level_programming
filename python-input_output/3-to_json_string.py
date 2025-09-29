#!/usr/bin/python3
"""Module pour JSON String"""
import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne JSON

    Args:
        my_obj (object): L'objet Python à convertir en JSON

    Returns:
        str: La chaîne JSON représentant l'objet
    """
    return json.dumps(my_obj)
