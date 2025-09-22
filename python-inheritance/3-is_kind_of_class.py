#!/usr/bin/python3
"""
Ce module définit la fonction is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance d’une classe
    ou une instance d’une sous-classe de cette classe.

    Arguments:
        obj: L’objet à vérifier.
        a_class: La classe avec laquelle comparer.

    Retourne:
        True si obj est une instance de a_class ou
        d’une sous-classe de a_class, sinon False.
    """
    return isinstance(obj, a_class)
