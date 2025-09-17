#!/usr/bin/python3
"""Module 7-rectangle
Ce module définit une classe Rectangle avec largeur, hauteur,
aire, périmètre, représentation en chaîne de caractères,
méthode __repr__ et compteur d’instances.
"""


class Rectangle:
    """Classe qui définit un rectangle avec largeur et hauteur.

    Attributs de classe :
        number_of_instances (int): Compteur des instances de Rectangle.
        print_symbol (any): Symbole utilisé pour l’affichage.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle.

        Args:
            width (int): largeur du rectangle (par défaut 0).
            height (int): hauteur du rectangle (par défaut 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Modifie la largeur du rectangle.

        Args:
            value (int): nouvelle largeur.

        Raises:
            TypeError: si width n’est pas un entier.
            ValueError: si width < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifie la hauteur du rectangle.

        Args:
            value (int): nouvelle hauteur.

        Raises:
            TypeError: si height n’est pas un entier.
            ValueError: si height < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l’aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle.

        Returns:
            int: périmètre ou 0 si largeur ou hauteur = 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une chaîne représentant le rectangle.

        Le rectangle est représenté avec le symbole print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width
                         for _ in range(self.__height))

    def __repr__(self):
        """Retourne une chaîne qui permet de recréer l’instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Affiche un message lors de la suppression du rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
