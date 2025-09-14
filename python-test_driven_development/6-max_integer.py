#!/usr/bin/python3
"""Module to find the max integer in a list
"""

# Définition de la fonction max_integer
def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
       If the list is empty, the function returns None
    """
    # Vérifie si la liste est vide
    if len(list) == 0:
        return None  # Si oui, renvoie None car il n’y a pas de maximum possible

    # Initialise la variable 'result' avec le premier élément de la liste
    result = list[0]

    # Déclare un index 'i' pour parcourir la liste à partir du deuxième élément
    i = 1
    while i < len(list):
        # Compare l’élément courant avec 'result'
        if list[i] > result:
            result = list[i]  # Si plus grand, met à jour 'result'
        i += 1  # Passe à l’élément suivant

    # Après la boucle, 'result' contient le plus grand entier de la liste
    return result
