#!/usr/bin/python3
"""
Ce module contient la définition de la classe Rectangle.
Il sert de base pour représenter un rectangle dans le contexte POO
"""


class Rectangle:
    """
    Classe représentant un rectangle.
    Elle contiendra des attributs.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Ceci est un attribut d'instance privée

        Args:
            width (int, optional): Définit la largeur. Defaults to 0.
            height (int, optional): définit la hauteur. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            perimeter = 0
            return perimeter

        perimeter = (self.width + self.height) * 2
        return perimeter

    def __str__(self):
        result = ""

        if self.width == 0 or self.height == 0:
            return result

        for i in range(self.height):
            result += '#' * self.width
            # Ajout d'un saut de ligne sauf pour la dernière ligne
            if i < self.height - 1:
                result += '\n'
        return result

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
