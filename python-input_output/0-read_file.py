#!/usr/bin/python3
"""Module contenant la fonction read_file"""

def read_file(filename=""):
    """
    Lit un fichier texte UTF-8 et affiche son contenu.

    Args:
        filename (str): Nom du fichier à lire. Par défaut, vide.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read(), end="")
