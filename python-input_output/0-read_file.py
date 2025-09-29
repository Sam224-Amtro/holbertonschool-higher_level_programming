#!/usr/bin/python3
"""Definit la fonction read"""

def read_file(filename=""):
    """
    Lit un fichier texte encodé en UTF-8 et affiche son contenu dans
    la sortie standard (stdout).

    Args:
        filename (str): Nom du fichier à lire. Par défaut, une chaîne vide.
    """

    # Le mot-clé "with" garantit que le fichier sera fermé automatiquement,
    # même en cas d'erreur (bonne pratique pour la gestion des fichiers).
    with open(filename, mode="r", encoding="utf-8") as file:

        # La méthode read() lit l’intégralité du contenu du
        # fichier en une seule fois.
        # Ici, on l’affiche directement avec print().
        # Le paramètre end="" empêche print d’ajouter un saut
        # de ligne supplémentaire,
        # car le fichier contient peut-être déjà des retours à la ligne.
        print(file.read(), end="")
