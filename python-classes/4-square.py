#!/usr/bin/python3
"""
Module 4-square
Définit une classe Square qui représente un carré.
"""


class Square:
    """
    Représente un carré.

    Attributs :
        __size (int) : La taille du carré (privé).
    """
    def __init__(self, size=0):
        """
        Initialise un nouveau carré.

        Arguments :
            size (int) : La taille du carré. Par défaut 0.

        Lève :
            TypeError : Si size n’est pas un entier.
            ValueError : Si size est inférieur à 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Récupère la taille du carré.

        Retourne :
            int : La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré.

        Arguments :
            value (int) : La nouvelle taille du carré.

        Lève :
            TypeError : Si value n’est pas un entier.
            ValueError : Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l’aire du carré.

        Retourne :
            int : L’aire du carré.
        """
        return self.__size ** 2
