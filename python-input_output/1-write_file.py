#!/usr/bin/python3
"""Define function Write file"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (UTF-8)
    et retourne le nombre de caractères écrits.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
