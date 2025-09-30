#!/usr/bin/python3
"""Module pour JSON"""
import json


def class_to_json(obj):
    """
    Retourne la description d’un objet sous forme de dictionnaire.
    """
    return obj.__dict__
