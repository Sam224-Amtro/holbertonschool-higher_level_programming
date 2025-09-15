#!/usr/bin/python3

class Carre:
    """Une classe qui définit un carré."""

    def __init__(self, taille=0):
        """
        Initialise le carré avec une taille optionnelle.

        Args:
            taille (int): La longueur du côté du carré. Par défaut 0.

        Raises:
            TypeError: Si taille n’est pas un entier.
            ValueError: Si taille est inférieure à 0.
        """
        if not isinstance(taille, int):
            raise TypeError("taille doit être un entier")
        if taille < 0:
            raise ValueError("taille doit être >= 0")
        self.__taille = taille

    def aire(self):
        """
        Calcule et retourne l’aire du carré.

        Returns:
            int: L’aire du carré.
        """
        return self.__taille ** 2
