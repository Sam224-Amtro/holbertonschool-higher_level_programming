#!/usr/bin/python3


class Square:
    """
    Représente un carré.

    Attributs :
        __size (int) : La taille du carré (privée).
        __position (tuple) : La position du carré sous forme
        de tuple (x, y) (privée).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un nouveau carré avec une taille et une position.

        Args :
            size (int) : La taille du carré (par défaut 0).
            position (tuple) : La position du carré (par défaut (0, 0)).

        Raises :
            TypeError : Si size n'est pas un entier ou position n'est pas
            un tuple de 2 entiers positifs.

            ValueError : Si size est inférieur à 0.
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Récupère la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré.

        Args :
            value (int) : La nouvelle taille.

        Raises :
            TypeError : Si value n'est pas un entier.
            ValueError : Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Récupère la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Définit la position du carré.

        Args :
            value (tuple) : Le nouveau tuple (x, y) de position.

        Raises :
            TypeError : Si value n'est pas un tuple de 2 entiers positifs.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calcule et retourne l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré en utilisant le caractère #.
        Respecte la position (x, y) pour le décalage horizontal et vertical.
        Si la taille est 0, affiche juste une ligne vide.
        """
        if self.size == 0:
            print()
            return

        # Décalage vertical
        for _ in range(self.__position[1]):
            print()

        # Affichage du carré avec décalage horizontal
        for _ in range(self.size):
            print(" " * self.__position[0] + "#" * self.__size)
