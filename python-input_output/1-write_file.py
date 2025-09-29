#!/usr/bin/python3
"""Define function Write file"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (UTF-8)
    et retourne le nombre de caractères écrits.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            return file.write(text)
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier '{filename}': {e}")
        return 0
