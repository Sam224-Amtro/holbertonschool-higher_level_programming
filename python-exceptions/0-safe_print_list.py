#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Compteur du nombre d'éléments réellement imprimés
    compteur = 0

    # On essaie d'imprimer x éléments
    for k in range(x):
        try:
            # On imprime l'élément sans retour à la ligne
            print(my_list[k], end="")
            # Si l'impression réussit, on incrémente le compteur
            compteur += 1
        except IndexError:
            # Si l'élément n'existe pas (IndexError), on arrête la boucle
            break
    # Impression d'un retour à la ligne après tous les éléments
    print()
    # On retourne le nombre réel d'éléments imprimés
    return (compteur)
