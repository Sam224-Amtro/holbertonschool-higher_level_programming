#!/usr/bin/python3
"""
Module 4-carré
Définit une classe Carré qui représente un carré.
"""


class Carre:
    """
    Représente un carré.

    Attributs :
        __taille (int): La taille du carré (privé).
    """
    def __init__(self, taille=0):
        """
        Initialise un nouveau carré.

        Args:
            taille (int): La taille du carré. Par défaut 0.

        Raises:
            TypeError: Si taille n’est pas un entier.
            ValueError: Si taille est inférieure à 0.
        """
        self.taille = taille

    @property
    def taille(self):
        """
        Récupère la taille du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__taille

    @taille.setter
    def taille(self, valeur):
        """
        Définit la taille du carré.

        Args:
            valeur (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si valeur n’est pas un entier.
            ValueError: Si valeur est inférieure à 0.
        """
        if not isinstance(valeur, int):
            raise TypeError("la taille doit être un entier")
        if valeur < 0:
            raise ValueError("la taille doit être >= 0")
        self.__taille = valeur

    def aire(self):
        """
        Calcule l’aire du carré.

        Returns:
            int: L’aire du carré.
        """
        return self.__taille ** 2
