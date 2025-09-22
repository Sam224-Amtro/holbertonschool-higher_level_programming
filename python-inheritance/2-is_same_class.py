#!/usr/bin/python3
"""Module documentation"""


def is_same_class(obj, a_class):
    """
    Renvoie True si 'objet' est exactement une instance de 'une_classe',
    sinon renvoie False.
    """
    return type(obj) is a_class
