#!/usr/bin/python3
"""
Module 11-square
Ce module définit une classe Square qui hérite de Rectangle.
"""

# Importation de la classe Rectangle depuis 9-rectangle.py
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Carré qui hérite de Rectangle."""

    def __init__(self, size):
        """Initialise un carré avec une taille donnée."""

        # Vérifie que size est un entier positif
        self.integer_validator("size", size)
        self.__size = size  # Attribut privé
        # Appelle le constructeur de la classe parente (Rectangle)
        super().__init__(size, size)

    def area(self):
        """Calcule et retourne l’aire du carré."""
        return self.__size ** 2

    def __str__(self):
        """Retourne une représentation sous forme de chaîne du carré."""
        return f"[Square] {self.__size}/{self.__size}"
