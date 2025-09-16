#!/usr/bin/python3
"""
Module 5-square
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

        Args :
            size (int) : La taille du carré. Par défaut 0.

        Raises :
            TypeError : Si size n'est pas un entier.
            ValueError : Si size est inférieur à 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Récupère la taille du carré.

        Returns :
            int : La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré.

        Args :
            value (int) : La nouvelle taille du carré.

        Raises :
            TypeError : Si value n'est pas un entier.
            ValueError : Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns :
            int : L'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré en utilisant le caractère #.

        Si la taille est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
