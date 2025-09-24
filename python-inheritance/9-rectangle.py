#!/usr/bin/python3
"""Définit une classe Rectangle qui hérite de BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe représentant un rectangle, héritée de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise une nouvelle instance de Rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        # Vérification des valeurs grâce à integer_validator de BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Attributs privés
        self.__width = width
        self.__height = height

    def area(self):
        """Calcule l'aire du rectangle.

        Returns:
            int: L'aire du rectangle (largeur × hauteur).
        """
        return self.__width * self.__height

    def __str__(self):
        """Renvoie la représentation en chaîne du rectangle.

        Returns:
            str: La description du rectangle au format [Rectangle] <largeur>/<hauteur>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
