#!/usr/bin/python3

class Carre:
    """Une classe qui définit un carré."""

    def __init__(self, taille=0):
        """Initialise le carré avec un attribut privé taille."""
        self.taille = taille

    @property
    def taille(self):
        """Récupère la taille du carré."""
        return self.__taille

    @taille.setter
    def taille(self, valeur):
        """Définit la taille du carré avec validation."""
        if not isinstance(valeur, int):
            raise TypeError("la taille doit être un entier")
        if valeur < 0:
            raise ValueError("la taille doit être >= 0")
        self.__taille = valeur

    def aire(self):
        """Calcule et renvoie l'aire du carré."""
        return self.__taille ** 2
