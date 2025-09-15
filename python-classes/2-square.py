#!/usr/bin/python3
"""
Module 2-square
Définit une classe Square qui représente un carré.
"""


class Square:
    """
    Représente un carré.

    Attributs :
        __size (int) : La taille du carré (privée).
    """

    def __init__(self, size=0):
        """
        Initialise un nouveau carré.

        Args:
            size (int, optionnel) : La taille du carré. Valeur par défaut 0.

        Raises:
            TypeError : Si size n'est pas un entier.
            ValueError : Si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
