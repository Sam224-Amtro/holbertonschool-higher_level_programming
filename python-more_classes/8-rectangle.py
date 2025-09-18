#!/usr/bin/python3
"""
Module Rectangle
Defines a class Rectangle
"""

class Rectangle:
    """Defines a rectangle."""

    # Attributs de classe
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructeur de la classe Rectangle.
        Initialise largeur et hauteur avec vérification,
        puis incrémente le compteur d'instances.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter : retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter : définit la largeur du rectangle.
        Vérifie que c’est un entier >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter : retourne la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter : définit la hauteur du rectangle.
        Vérifie que c’est un entier >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l’aire du rectangle (largeur × hauteur)."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Retourne le périmètre du rectangle.
        Si largeur ou hauteur = 0 → retourne 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une représentation "graphique" du rectangle,
        composée du symbole défini dans print_symbol.
        Si largeur ou hauteur = 0 → retourne une chaîne vide.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])

    def __repr__(self):
        """
        Retourne une chaîne permettant de recréer
        le rectangle avec eval().
        Exemple : Rectangle(3, 4)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Méthode appelée à la suppression de l’instance.
        Décrémente le compteur d’instances et affiche un message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Méthode statique qui compare deux rectangles en fonction de leur aire.
        Retourne le plus grand, ou rect_1 si les deux ont la même aire.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
