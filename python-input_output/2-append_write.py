#!/usr/bin/python3
"""Define function Write file"""


def append_write(filename="", text=""):
    """
    Ajoute du texte à la fin d'un fichier et retourne le nombre
    de caractères ajoutés.
    """
    # Ouvre le fichier en mode ajout ("a"), UTF-8
    with open(filename, "a", encoding="utf-8") as file:
        # Écrit le texte et retourne le nombre de caractères ajoutés
        return file.write(text)
