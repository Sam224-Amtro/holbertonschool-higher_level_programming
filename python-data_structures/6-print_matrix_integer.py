#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Définition de la fonction, avec une valeur par défaut "matrix=[[]]"
    # qui représente une matrice vide (liste contenant une liste vide).

    for row in matrix:
        # On parcourt la matrice ligne par ligne.
        # Exemple: si matrix = [[1,2,3],[4,5,6]], alors
        # row sera [1,2,3] puis [4,5,6].

        for k in range(len(row)):
            # On parcourt chaque élément de la ligne avec son index.
            # range(len(row)) génère les indices [0, 1, 2, ...].

            print("{:d}".format(row[k]), end="")
            # On affiche l’élément entier au format décimal {:d}.
            # end="" évite que print ajoute un retour à la ligne automatique.

            if k < len(row) - 1:
                print(" ", end="")
                # Si ce n’est pas le dernier élément de la ligne,
                # on affiche un espace " " après le nombre.
                # Ça évite d’avoir un espace à la fin de la ligne.

        print()
        # Quand la ligne est terminée, on fait un retour à la ligne
        # pour passer à la ligne suivante de la matrice.
