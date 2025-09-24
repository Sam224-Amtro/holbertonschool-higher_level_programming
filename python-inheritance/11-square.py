#!/usr/bin/python3
"""
Module 11-square.
Contient la classe Square qui hérite de Rectangle.
"""


# Importation de Rectangle depuis 9-rectangle.py
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Carré qui hérite de Rectangle."""

    def __init__(self, size):
        """Initialise une nouvelle instance de Carré."""
        self.integer_validator("size", size)
        self.__size = size
        # Appelle le constructeur de la classe parente
        super().__init__(size, size)

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

    def __str__(self):
        """Retourne la représentation sous forme de chaîne du carré."""
        return f"[Square] {self.__size}/{self.__size}"
