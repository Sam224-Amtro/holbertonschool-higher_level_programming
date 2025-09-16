#!/usr/bin/python3
"""
Module 5-carre
Définit une classe Carré qui représente un carré.
"""


class Carre:
    """
    Représente un carré.

    Attributs :
        __taille (int) : La taille du côté du carré (privé).
    """

    def __init__(self, taille=0):
        """
        Initialise un nouveau carré.

        Arguments :
            taille (int) : La taille du côté du carré. Par défaut 0.

        Lève :
            TypeError : Si taille n’est pas un entier.
            ValueError : Si taille est inférieur à 0.
        """
        self.taille = taille

    @property
    def taille(self):
        """
        Récupère la taille du côté du carré.

        Retourne :
            int : La taille du côté du carré.
        """
        return self.__taille

    @taille.setter
    def taille(self, valeur):
        """
        Définit la taille du côté du carré.

        Arguments :
            valeur (int) : La nouvelle taille du côté du carré.

        Lève :
            TypeError : Si valeur n’est pas un entier.
            ValueError : Si valeur est inférieur à 0.
        """
        if not isinstance(valeur, int):
            raise TypeError("la taille doit être un entier")
        if valeur < 0:
            raise ValueError("la taille doit être >= 0")
        self.__taille = valeur

    def aire(self):
        """
        Calcule l’aire du carré.

        Retourne :
            int : L’aire du carré.
        """
        return self.__taille ** 2

    def afficher(self):
        """
        Affiche le carré avec le caractère #.

        Si la taille est 0, affiche une ligne vide.
        """
        if self.__taille == 0:
            print("")
        else:
            for _ in range(self.__taille):
                print("#" * self.__taille)
