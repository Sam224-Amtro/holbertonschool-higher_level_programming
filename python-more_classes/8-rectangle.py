#!/usr/bin/python3
"""
Module Rectangle
Définit une classe Rectangle
"""


class Rectangle:
    """Définit un rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise une nouvelle instance de Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Récupère la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur avec validation."""
        if not isinstance(value, int):
            raise TypeError("width doit être un entier")
        if value < 0:
            raise ValueError("width doit être >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur avec validation."""
        if not isinstance(value, int):
            raise TypeError("height doit être un entier")
        if value < 0:
            raise ValueError("height doit être >= 0")
        self.__height = value

    def area(self):
        """Retourne l’aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une représentation du rectangle
        avec le symbole print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) *
                          self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Retourne une représentation de l’objet
        permettant de recréer une nouvelle instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Affiche un message lors de la suppression
        d’une instance de Rectangle et décrémente le compteur.
        """
        Rectangle.number_of_instances -= 1
        print("Au revoir rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Retourne le rectangle le plus grand basé sur l’aire."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 doit être une instance de Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 doit être une instance de Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
