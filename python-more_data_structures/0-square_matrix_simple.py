#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [] # nouvelle matrice vide qui contiendra le résultat

    for ligne in matrix: # on parcourt chaque ligne de la matrice originale
        new_ligne = [] # on crée une nouvelle ligne vide
        for x in ligne: # on parcourt chaque élément de la ligne
            new_ligne.append(x ** 2) # on ajoute le carré de l’élément
        new_matrix.append(new_ligne) # on ajoute la nouvelle ligne à la matrice

    return new_matrix # on retourne la nouvelle matrice sans modifier l’originale
