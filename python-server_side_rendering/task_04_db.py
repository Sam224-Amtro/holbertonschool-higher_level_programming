#!/usr/bin/python3
"""
Task 4 - Displaying Data from JSON, CSV, and SQLite in Flask
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# ---------- FONCTIONS DE LECTURE DES SOURCES ----------

def read_json_file(filename):
    """Lit un fichier JSON et renvoie une liste de produits"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_file(filename):
    """Lit un fichier CSV et renvoie une liste de produits"""
    products = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                except (ValueError, KeyError):
                    pass
                products.append(row)
    except FileNotFoundError:
        return []
    return products

def read_sqlite_db(filename):
    """Lit la base SQLite et renvoie une liste de produits"""
    products = []
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except sqlite3.Error:
        return []
    return products

# ---------- ROUTE PRINCIPALE ----------

@app.route('/products')
def products():
    """
    Affiche les produits selon la source (json, csv, sql)
    et filtre optionnellement par ?id=
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    products = []
    error_message = None

    # Sélection de la source
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_db('products.db')
    else:
        error_message = "Wrong source. Please use ?source=json, ?source=csv, or ?source=sql."

    # Filtrage par ID
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
