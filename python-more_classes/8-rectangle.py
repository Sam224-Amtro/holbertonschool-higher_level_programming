#!/usr/bin/python3
"""
Module Rectangle
Définit une classe Rectangle
"""


class Rectangle:
    """Définit un rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, largeur=0, hauteur=0):
        """Initialise une nouvelle instance de Rectangle."""
        self.largeur = largeur
        self.hauteur = hauteur
        Rectangle.number_of_instances += 1

    @property
    def largeur(self):
        """Récupère la largeur."""
        return self.__largeur

    @largeur.setter
    def largeur(self, valeur):
        """Définit la largeur avec validation."""
        if not isinstance(valeur, int):
            raise TypeError("la largeur doit être un entier")
        if valeur < 0:
            raise ValueError("la largeur doit être >= 0")
        self.__largeur = valeur

    @property
    def hauteur(self):
        """Récupère la hauteur."""
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, valeur):
        """Définit la hauteur avec validation."""
        if not isinstance(valeur, int):
            raise TypeError("la hauteur doit être un entier")
        if valeur < 0:
            raise ValueError("la hauteur doit être >= 0")
        self.__hauteur = valeur

    def aire(self):
        """Retourne l’aire du rectangle."""
        return self.__largeur * self.__hauteur

    def perimetre(self):
        """Retourne le périmètre du rectangle."""
        if self.__largeur == 0 or self.__hauteur == 0:
            return 0
        return 2 * (self.__largeur + self.__hauteur)

    def __str__(self):
        """
        Retourne une représentation en chaîne du
        rectangle avec print_symbol.
        """
        if self.__largeur == 0 or self.__hauteur == 0:
            return ""
        return "\n".join([str(self.print_symbol) *
                          self.__largeur for _ in range(self.__hauteur)])

    def __repr__(self):
        """
        Retourne une représentation en chaîne du
        rectangle pour recréer une nouvelle instance.
        """
        return f"Rectangle({self.__largeur}, {self.__hauteur})"

    def __del__(self):
        """
        Affiche un message quand une instance de
        Rectangle est supprimée et décrémente le compteur.
        """
        Rectangle.number_of_instances -= 1
        print("Au revoir rectangle...")

    @staticmethod
    def plus_grand_ou_egal(rect_1, rect_2):
        """Retourne le plus grand rectangle basé sur l’aire."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 doit être une instance de Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 doit être une instance de Rectangle")
        if rect_1.aire() >= rect_2.aire():
            return rect_1
        return rect_2
