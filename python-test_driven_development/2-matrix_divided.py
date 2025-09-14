#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix (list): liste de listes contenant uniquement des entiers ou des flottants
        div (int or float): nombre par lequel diviser

    Raises:
        TypeError: si div n’est pas un nombre
        ZeroDivisionError: si div est égal à zéro
        TypeError: si matrix n’est pas une liste de listes d’int ou de float
        TypeError: si chaque ligne de la matrix n’a pas la même taille
        TypeError: si les éléments de la matrix ne sont pas des int ou float

    Returns:
        list: une nouvelle matrice avec les éléments divisés par div et arrondis à 2 décimales
    """

    # Vérifie que div est bien un nombre (int ou float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Interdit la division par zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Vérifie que matrix est une liste non vide
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Vérifie que chaque élément de matrix est bien une liste
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Vérifie que toutes les lignes de la matrice ont la même longueur
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        # Vérifie que chaque élément de la ligne est un entier ou un flottant
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Une fois toutes les vérifications terminées, on construit une nouvelle matrice
    new_matrix = []

    # On parcourt chaque ligne de la matrice
    for k in matrix:
        nouvelle_ligne = []
        # On divise chaque élément de la ligne par div et on arrondit à 2 décimales
        for element in k:
            res = round(element / div, 2)
            nouvelle_ligne.append(res)
        # On ajoute la nouvelle ligne dans la nouvelle matrice
        new_matrix.append(nouvelle_ligne)

    # Retourne la nouvelle matrice
    return new_matrix
