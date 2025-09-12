#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # Fonction qui affiche les entiers présents dans une liste
    # my_list : la liste donnée
    # x : nombre d’éléments de la liste à tester

    compteur = 0  # Compte combien d'entiers ont été affichés

    for k in range(x):  # Parcourt les x premiers éléments
        try:
            print("{:d}".format(my_list[k]), end="")
            # Affiche l’élément si c’est un entier
            compteur += 1  # On ajoute +1 si affichage réussi
        except (TypeError, ValueError):
            # Si ce n’est pas un entier, on passe au suivant
            continue

        print()  # Retour à la ligne après l’affichage

        return compteur  # ATTENTION : placé ici, la fonction s’arrête trop tôt
