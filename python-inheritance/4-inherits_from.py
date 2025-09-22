#!/usr/bin/python3
"""
Ce module définit la fonction inherits_from.
"""

def inherits_from(obj, a_class):
    """
    Renvoie True si l'objet est une instance d'une classe qui hérite
    (directement ou indirectement) de la classe spécifiée ;
    sinon, renvoie False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
