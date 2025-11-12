#!/usr/bin/python3
"""
Flask App - Task 3: Displaying Data from JSON or CSV Files
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# --- Fonctions utilitaires ---

def read_json_file(filename):
    """Lit un fichier JSON et renvoie une liste de produits"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_file(filename):
    """Lit un fichier CSV et renvoie une liste de produits"""
    products = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convertir les types
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                except (ValueError, KeyError):
                    pass
                products.append(row)
    except FileNotFoundError:
        return []
    return products

# --- Route principale ---

@app.route('/products')
def products():
    """
    Affiche les produits depuis un fichier JSON ou CSV
    selon le paramètre ?source=
    Optionnellement filtre par ?id=
    """

    # Récupération des paramètres de requête
    source = request.args.get('source')
    product_id = request.args.get('id')

    products = []
    error_message = None

    # Lecture selon la source
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        error_message = "Wrong source. Please use ?source=json or ?source=csv."

    # Filtrage par ID (si applicable)
    if product_id and not error_message:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if int(p.get("id", 0)) == product_id]
            if filtered:
                products = filtered
            else:
                error_message = "Product not found."
                products = []
        except ValueError:
            error_message = "Invalid ID format. ID must be an integer."
            products = []

    # Rendu du template
    return render_template('product_display.html',
                           products=products,
                           error=error_message,
                           source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
