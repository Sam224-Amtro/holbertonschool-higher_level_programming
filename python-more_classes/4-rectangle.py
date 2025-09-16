#!/usr/bin/python3

class Rectangle:
    """Classe qui définit un rectangle avec une largeur et une hauteur."""

    def __init__(self, width=0, height=0):
        """
        Constructeur de la classe Rectangle.

        Args:
            width (int, optionnel): largeur du rectangle (par défaut 0).
            height (int, optionnel): hauteur du rectangle (par défaut 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter de l'attribut privé __width.

        Returns:
            int: la largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter de l'attribut privé __width.

        Args:
            value (int): nouvelle valeur pour la largeur.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter de l'attribut privé __height.

        Returns:
            int: la hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter de l'attribut privé __height.

        Args:
            value (int): nouvelle valeur pour la hauteur.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: aire (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: périmètre (2 * (width + height)),
                 ou 0 si width ou height est nul.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Représentation en chaîne de caractères du rectangle,
        affichée avec le caractère '#'.

        Returns:
            str: rectangle dessiné avec '#',
                 ou chaîne vide si width ou height est nul.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """
        Représentation officielle de l'objet Rectangle.

        Returns:
            str: chaîne de type "Rectangle(width, height)"
                 qui permet de recréer l'objet avec eval().
        """
        return f"Rectangle({self.width}, {self.height})"
