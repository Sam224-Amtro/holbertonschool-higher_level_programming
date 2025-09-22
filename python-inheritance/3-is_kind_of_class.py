#!/usr/bin/python3
"""Module documentation"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance de la classe spécifiée,
    ou bien une instance d’une classe qui hérite de celle-ci.

    Arguments :
        objet : L’objet à vérifier.
        une_classe : La classe de référence.

    Retourne :
        True si 'objet' est une instance de 'une_classe' ou d’une sous-classe,
        sinon False.
    """
    return isinstance(obj, a_class)
