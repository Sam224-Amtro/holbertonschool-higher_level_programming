#!/usr/bin/python3
"""
Module contenant la fonction matrix_divided
qui divise tous les éléments d'une matrice par un diviseur donné.
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un nombre.

    Args:
        matrix (list): liste de listes d'entiers ou de flottants.
        div (int ou float): nombre par lequel diviser les éléments.

    Raises:
        TypeError: si matrix n’est pas une liste de listes d’int/float.
        TypeError: si les lignes de la matrice n’ont pas la même taille.
        TypeError: si div n’est pas un nombre.
        ZeroDivisionError: si div est égal à 0.

    Returns:
        list: une nouvelle matrice avec les résultats arrondis à 2 décimales.
    """

    # Vérification du diviseur
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Vérification de la matrice
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Construction de la nouvelle matrice
    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

    return new_matrix
