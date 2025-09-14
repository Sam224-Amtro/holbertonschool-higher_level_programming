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
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)) or div == float("inf"):
        raise TypeError("div must be a number")

    for ligne in matrix:
        if len(matrix[0]) != len(ligne):
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

    try:
        new_mat = []
        for ligne in matrix:
            new_mat.append(list(map(lambda x: round(x / div, 2), ligne)))
        return new_mat
    except (TypeError, ValueError) as e:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
