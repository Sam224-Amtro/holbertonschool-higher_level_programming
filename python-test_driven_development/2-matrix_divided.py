#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals."""

    # Vérifier que matrix est une liste de listes
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Vérifier que tous les éléments sont des nombres
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Vérifier que toutes les lignes ont la même taille
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Vérifier div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Créer une nouvelle matrice avec les valeurs divisées
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
