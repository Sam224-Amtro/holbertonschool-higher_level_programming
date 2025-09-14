#!/usr/bin/python3
"""
Module Matrix divided

Functions:
    matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.
    matrix must be a list of lists of integers or floats.
    Each row of the matrix must have the same size.
    div must be a number (integer or float) and can't be equal to 0.
    Returns a new matrix, else raises TypeError or ZeroDivisionError.
    """
    # Vérification de la validité de la matrice
    if (
        not matrix
        or not all(isinstance(ligne, list) for ligne in matrix)
        or not all(
            all(isinstance(x, (int, float)) for x in ligne) for ligne in matrix
            )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Vérification que toutes les lignes ont la même taille
    row_length = len(matrix[0])
    for ligne in matrix:
        if len(ligne) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Vérification du diviseur
    if not isinstance(div, (int, float)) or div == float("inf"):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Création de la nouvelle matrice
    new_mat = [
        [round(x / div, 2) for x in ligne]
        for ligne in matrix
    ]

    return new_mat
