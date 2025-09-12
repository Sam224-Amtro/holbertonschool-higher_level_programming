#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    # Compteur pour savoir combien d’éléments ont vraiment été affichés
    count = 0

    # On parcourt de 0 jusqu’à x-1
    for i in range(x):
        # Vérifie si l’index existe dans la liste (évite une erreur IndexError)
        if i < len(my_list):
            print(my_list[i], end="")  # affiche l’élément sans saut de ligne
            count += 1                 # on incrémente le compteur
        else:
            break  # si on dépasse la taille de la liste, on arrête la boucle

    print()  # saut de ligne final pour que l’affichage soit propre

    # Retourne le nombre d’éléments effectivement affichés
    return count
