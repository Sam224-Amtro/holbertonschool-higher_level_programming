#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry.
"""

# Import de la classe parente BaseGeometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe qui représente un rectangle.
    Hérite de BaseGeometry pour profiter de la validation des entiers.
    """

    def __init__(self, width, height):
        """
        Constructeur de Rectangle.

        Args:
            width (int): largeur du rectangle (doit être > 0)
            height (int): hauteur du rectangle (doit être > 0)
        """
        # Validation des valeurs avec la méthode héritée de BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Stockage en attributs privés
        self.__width = width
        self.__height = height
