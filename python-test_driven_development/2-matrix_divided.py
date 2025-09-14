#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix (list): list of lists
        div (int or float): number

    Raises:
        TypeError: div doit être un nombre
        ZeroDivisionError: div ne peut pas être égal à zéro
        TypeError: la matrix doit être une liste de listes d'int ou float
        TypeError: la matrix doit être une liste de listes d'int ou float
        TypeError: chaque ligne de la matrix doit être de la même taille
        TypeError: la matrix doit être une liste de listes d'int ou float

    Returns:
        _type_: nouvelle matrix
    """
    row = None

    # Vérifie que div est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Vérifie que matrix est une liste de liste
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Vérifie la taille des lignes
    row_lenght = len(matrix[0])
    for row in matrix:
        if len(row) != row_lenght:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Vérification fini, place à la division et la nouvelle matrix !
    new_matrix = []
    element = None

    for i in matrix:
        nouvelle_ligne = []
        for element in i:
            res = round(element / div, 2)
            nouvelle_ligne.append(res)
        new_matrix.append(nouvelle_ligne)
    return new_matrix
