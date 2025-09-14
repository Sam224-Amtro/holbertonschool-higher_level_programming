#!/usr/bin/python3

"""
    Prints the full name in the format: My name is <first name> <last name>.
    # Docstring globale du fichier : explique l’objectif général du script
"""

# Définition de la fonction say_my_name
def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format: My name is <first name> <last name>.

    Args:
        # Argument obligatoire : prénom
        first_name: The first name (must be a string).
        # Argument optionnel : nom (par défaut vide)
        last_name: The last name (optional, must be a string).

    Raises:
        # Gestion des erreurs si mauvais type
        TypeError: If first_name or last_name is not a string.
    """

    # Vérifie que first_name est bien une chaîne de caractères
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Vérifie que last_name est bien une chaîne de caractères
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Affiche le nom complet au format demandé
    # f-string permet d’insérer directement les variables dans la chaîne
    # strip() enlève les espaces inutiles si last_name est vide
    print(f"My name is {first_name} {last_name}".strip())
