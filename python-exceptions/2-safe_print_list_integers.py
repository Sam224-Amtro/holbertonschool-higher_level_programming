#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # Fonction qui affiche les entiers présents dans une liste
    # my_list : la liste donnée
    # x : nombre d’éléments de la liste à tester

    compteur = 0  # Initialise le compteur d'entiers affichés

    # Parcourt les x premiers éléments de la liste
    for k in range(x):
        try:
            # Tente d'afficher l'élément s'il est un entier
            print("{:d}".format(my_list[k]), end="")
            compteur += 1  # Incrémente le compteur si affichage réussi
        except (TypeError, ValueError):
            # Si l'élément n'est pas un entier, on l'ignore
            continue

    print()  # Ajoute un retour à la ligne après l'affichage
    return compteur  # Retourne le nombre total d'entiers affichés
