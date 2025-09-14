#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int/float): number to divide by

    Returns:
        new matrix (list of lists): each element divided by div

    Raises:
        TypeError: if matrix is not a list of lists of int/float
        TypeError: if rows are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div == 0
    """

    # Vérification que matrix est une liste de listes
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que toutes les lignes ont la même taille
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérification du diviseur
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Retourne une nouvelle matrice avec division arrondie à 2 décimales
    return [[round(num / div, 2) for num in row] for row in matrix]
