#!/usr/bin/python3
"""Functions to fetch, print and save posts"""

# Importation des modules nécessaires
import requests  # Pour envoyer des requetes HTTP (GET, POST, etc)
import csv  # Pour écrire et lire des fichiers CSV

# Fonction 1 : récuperer et afficher les titres des posts
def fetch_and_print_posts():
    # URL de l'API (fournit de faux posts pour les tests)
    url = "https://jsonplaceholder.typicode.com/posts"

    # Envoi d'une requète GET à l'API
    response = requests.get(url)

    # Affiche le code de status HTTP (200 = succès)
    print("Status Code:", response.status_code)

    # Si la requête s'est bien passée (code 200)
    if response.status_code == 200:
        # Convertit la reponse JSON en liste de dictionnaires python
        data = response.json()

        # Parcourt chaque post et affiche son titre
        for post in data:
            print(post["title"])
    else:
        # Si la requête a échoué, affiche un message d'erreur
        print("Failed to fetch posts.")

# Fonction 2 : récupérer et sauvegarder les posts dans un CSV
def fetch_and_save_posts():
    # Même URL de l'API
    url = "https://jsonplaceholder.typicode.com/posts"

    # Envoi d'une requête GET pour récupérer les posts
    response = requests.get(url)

    # Vérifie si la requête a réussi
    if response.status_code == 200:
        # convertit la réponse JSON en objet python
        data = response.json()

        # Crée une liste de dictionnaires ne contenant que
        # les champs "id", "title" et "body"
        posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]

        # Ouvrir (ou crée) un fichier CSV en mode écriture
        # newline="" évite les lignes vides entre les enregistrements
        # encoding="utf-8" gère les caractères spéciaux
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            # Définition de l'écrivain CSV avec les noms de colonnes
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            # Écrit la ligne d'en-tête (noms des colonnes)
            writer.writeheader()

            # Écrit toutes les lignes du fichier à partir de la liste 'posts'
            writer.writerows(posts)

        # Message de confirmation
        print("Posts saved to posts.csv")
    else:
        # Message d'erreur si la requête a échoué
        print("Failed to fetch posts.")
