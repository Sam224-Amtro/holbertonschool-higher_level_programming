#!/usr/bin/python3
"""Module qui joint deux tables : State et City"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    # Connexion à la base MySQL (avec user, mot de passe et nom de base en arguments)
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True   # Vérifie que la connexion est toujours active
    )

    # Crée les tables si elles n’existent pas déjà
    Base.metadata.create_all(engine)

    # Ouvre une session avec la base
    session = Session(engine)

    # Fait une requête qui joint les tables City et State
    # Trie les résultats par ID de ville (croissant)
    # Pour chaque paire (ville, état), affiche : "nom_état: (id_ville) nom_ville"
    for city, state in session.query(
        City, State).join(State).order_by(City.id.asc()).all():
        print(f'{state.name}: ({city.id}) {city.name}'
    )

    # Ferme la session après utilisation
    session.close()
