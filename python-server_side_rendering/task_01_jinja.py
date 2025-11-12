#!/usr/bin/python3
"""
Flask App for Task 1 - Basic Jinja Template Rendering
"""

from flask import Flask, render_template

# Création de l’application Flask
app = Flask(__name__)

# --- Route pour la page d’accueil ---
@app.route('/')
def home():
    """Affiche la page d’accueil"""
    return render_template('index.html')

# --- Route pour la page "About" ---
@app.route('/about')
def about():
    """Affiche la page À propos"""
    return render_template('about.html')

# --- Route pour la page "Contact" ---
@app.route('/contact')
def contact():
    """Affiche la page Contact"""
    return render_template('contact.html')

# --- Lancement de l’application ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
