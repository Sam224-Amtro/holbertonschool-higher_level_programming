#!/usr/bin/python3
"""
Flask App - Task 2: Dynamic Template with Loops and Conditions
"""

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    """Page d’accueil simple"""
    return "<h1>Welcome! Visit /items to see dynamic content.</h1>"

@app.route('/items')
def items():
    """Affiche une page avec une liste d’éléments chargés depuis un fichier JSON"""

    try:
        # Lecture du fichier JSON
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"items": []}  # Fichier manquant → liste vide
    except json.JSONDecodeError:
        data = {"items": []}  # Fichier corrompu → liste vide

    # Récupération de la liste d’items (ou liste vide par défaut)
    items_list = data.get("items", [])

    # Rendu du template avec la liste d’items passée à Jinja
    return render_template("items.html", items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
