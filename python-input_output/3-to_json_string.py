#!/usr/bin/python3
"""C'est pour JSON String"""


# Importe le module 'json' qui permet de travailler avec
# le format JSON en Python.
import json

def to_json_string(my_obj):
    """Renvoie une chaîne des fichiers JSON"""
    return json.dumps(my_obj)
