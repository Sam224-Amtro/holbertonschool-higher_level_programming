#!/usr/bin/python3
"""Definit Pascal's Triangle"""

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle up to level n."""
    # Cette fonction prend un entier n et retourne le triangle de Pascal
    # sous forme d'une liste de listes, jusqu'au niveau n (n lignes).

    if n <= 0:
        return []
        # Si n est inférieur ou égal à 0, le triangle n'a pas de lignes,
        # donc on retourne une liste vide.

    triangle = [[1]]
    # On initialise le triangle avec la première ligne,
    # qui contient toujours un seul 1.

    for i in range(1, n):
        # On boucle de la deuxième ligne (i=1) jusqu'à la n-ième ligne.
        prev_row = triangle[-1]
        # On récupère la dernière ligne du triangle
        # (celle construite précédemment).

        new_row = [1]
        # On commence la nouvelle ligne avec un 1, qui est toujours
        # le premier élément.

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
            # Chaque élément intermédiaire de la nouvelle ligne est la somme
            # de deux éléments adjacents de la ligne précédente.

        new_row.append(1)
        # On termine la nouvelle ligne avec un 1, qui est toujours
        # le dernier élément.

        triangle.append(new_row)
        # On ajoute la nouvelle ligne au triangle.

    return triangle
    # On retourne le triangle complet sous forme de liste de listes.
