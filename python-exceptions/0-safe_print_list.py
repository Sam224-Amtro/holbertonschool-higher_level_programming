#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Affiche au plus `x` éléments d’une liste
    et retourne combien ont été affichés.
    """

    # Initialiser le compteur d'éléments affichés
    count = 0

    # Parcourir les éléments jusqu'à x ou la fin de la liste
    for i in range(min(x, len(my_list))):
        print(my_list[i], end="")   # Affiche l’élément sans retour à la ligne
        count += 1                  # Incrémenter le compteur

    # Ajouter un saut de ligne à la fin
    print()

    # Retourner le nombre d’éléments affichés
    return count
