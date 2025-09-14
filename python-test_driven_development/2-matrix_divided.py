#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""

import math


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix (list): list of lists of integers/floats
        div (int or float): number

    Raises:
        TypeError: div must be a number (finite int or float)
        ZeroDivisionError: div cannot be zero
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size

    Returns:
        list: new matrix with elements divided and rounded to 2 decimals
    """

    # Vérifie que div est un nombre fini
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if math.isnan(div) or math.isinf(div):
        raise TypeError("div must be a finite number")

    # Vérifie que matrix est une liste de listes
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Vérifie la taille des lignes et les types des éléments
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
