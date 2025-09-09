#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Fonction qui retourne une nouvelle matrice
    # où chaque élément est le carré de l’élément original.
    # Paramètre :
    #   matrix : une liste de listes (matrice 2D)
    # Retour :
    #   une nouvelle matrice avec les mêmes dimensions,
    #   mais contenant les carrés des valeurs

    new_matrix = []  # on crée une nouvelle matrice vide qui contiendra le résultat

    for ligne in matrix:  # on parcourt chaque ligne de la matrice originale
        new_ligne = []    # on crée une nouvelle ligne vide
        for x in ligne:   # on parcourt chaque élément de la ligne
            new_ligne.append(x ** 2)  # on ajoute le carré de l’élément dans la nouvelle ligne
        new_matrix.append(new_ligne)  # on ajoute la nouvelle ligne dans la nouvelle matrice

    return new_matrix  # on retourne la nouvelle matrice sans modifier l’originale
