#!/usr/bin/python3
"""Definit Pascal's Triangle"""

def triangle_pascal(n):
    """
    Génère le triangle de Pascal jusqu'à n lignes.

    Args:
        n (int): Le nombre de lignes du triangle de Pascal.

    Returns:
        list: Une liste de listes représentant le triangle de Pascal.
    """
    if n <= 0:
        return []  # Retourne une liste vide si n est inférieur ou égal à 0

    triangle = []  # Initialise le triangle comme une liste vide

    for i in range(n):
        # Crée une nouvelle ligne avec 1 au début
        ligne = [1]

        # Remplit les valeurs du milieu de la ligne
        if i > 0:
            for j in range(1, i):
                # Chaque valeur est la somme des deux valeurs au-dessus
                ligne.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Ajoute 1 à la fin de la ligne si ce n'est pas la première ligne
        if i > 0:
            ligne.append(1)

        # Ajoute la ligne au triangle
        triangle.append(ligne)

    return triangle

