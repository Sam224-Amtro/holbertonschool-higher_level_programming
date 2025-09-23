#!/usr/bin/python3
"""Module for base_geometry class."""


class BaseGeometry:
    """A class for basic geometric operations."""

    def area(self):
        """Raises une exception indiquant que la méthode n'est pas
        implémenté."""
        raise Exception("area() n'est pas implémenté")

    def integer_validator(self, name, value):
        """
        Valide que la valeur est un entier et supérieur à 0.

        Args:
            name (str): Le nom de la valeur (utilisé dans l'exception
        message.)
            value (int): La valeur à valider.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure ou égale à 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} Doit être un entier")
        if value <= 0:
            raise ValueError(f"{name} doit être supérieur à 0")
