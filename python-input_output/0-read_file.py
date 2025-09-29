#!/usr/bin/python3
"""Module qui définit la fonction read_file"""

def read_file(filename=""):
    """
    Lit un fichier texte encodé en UTF-8 et affiche son contenu dans
    la sortie standard (stdout).

    Args:
        filename (str): Nom du fichier à lire. Par défaut, une chaîne vide.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
