#!/usr/bin/python3
"""
Module that defines the function matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int/float): number to divide by

    Returns:
        list of lists: new matrix with each value divided by div

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if rows are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div == 0
    """

    # Vérification du diviseur
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Vérification que matrix est une liste de listes non vide
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Vérification que toutes les lignes ont la même taille
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Calcul du résultat (arrondi à 2 décimales)
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(num / div, 2) for num in row])

    return new_matrix
