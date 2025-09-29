#!/usr/bin/python3
"""Define function Write file"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (UTF-8)
    et retourne le nombre de caractères écrits.

    Args:
        filename (str): Nom du fichier dans lequel écrire.
        text (str): Texte à écrire dans le fichier.

    Returns:
        int: Nombre de caractères écrits, ou 0 si une erreur survient.
    """
    try:
        # Ouverture du fichier en mode écriture avec encodage UTF-8
        with open(filename, "w", encoding="utf-8") as file:
            # Écriture et retour du nombre de caractères
            return file.write(text)
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier '{filename}': {e}")
        return 0
