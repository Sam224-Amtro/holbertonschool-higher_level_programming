#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Affiche jusqu’à `x` éléments d’une liste
    et retourne combien ont été affichés.
    """

# Compteur du nombre d'éléments effectivement affichés
    count = 0

    # Parcours des indices de 0 à x-1
    for i in range(x):
        # Vérifie si l'indice est valide dans la liste
        if i < len(my_list):
            # Affiche l'élément sans retour à la ligne
            print(my_list[i], end="")
            # Incrémente le compteur
            count += 1
        else:
            # Si on dépasse la taille de la liste, on arrête la boucle
            break

    # Ajoute un saut de ligne après l'affichage
    print()

    # Retourne le nombre d'éléments réellement affichés
    return count
