#!/usr/bin/python3

class Square:
    """Une classe qui définit un carré."""

    def __init__(self, size=0):
        """
        Constructeur de la classe Square.

        Paramètres :
            size (int) : La taille du côté du carré (par défaut 0).

        On passe par le setter pour profiter de la validation des données.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter pour récupérer la taille du carré.

        Retourne :
            int : La taille actuelle (côté du carré).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour modifier la taille du carré avec validation.

        Paramètres :
            value (int) : Nouvelle taille à attribuer.

        Exceptions :
            TypeError : si value n'est pas un entier.
            ValueError : si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Méthode pour calculer l’aire du carré.

        Retourne :
            int : Aire du carré (côté × côté).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Méthode pour afficher le carré avec le caractère `#`.

        - Si size = 0 : affiche une ligne vide.
        - Sinon : affiche un carré formé de `#`,
          de dimensions size × size.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
