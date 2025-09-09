#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Crée une nouvelle matrice vide qui contiendra le résultat
    new_matrix = []

    # On parcourt chaque ligne de la matrice originale
    for ligne in matrix:
        # On crée une nouvelle ligne vide
        new_ligne = []
        # On parcourt chaque élément de la ligne
        for x in ligne:
            # On ajoute le carré de l’élément
            new_ligne.append(x ** 2)
        # On ajoute la nouvelle ligne à la matrice
        new_matrix.append(new_ligne)

    # On retourne la nouvelle matrice sans modifier l’originale
    return new_matrix
