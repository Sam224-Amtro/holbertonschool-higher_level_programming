#!/usr/bin/python3
"""
Relie la classe State à la table dans la base de données et met à jour un enregistrement
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Connexion à la base MySQL (avec user, mot de passe et nom de base en arguments)
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    # Crée la table si elle n’existe pas
    Base.metadata.create_all(engine)

    # Ouvre une session avec la base
    session = Session(engine)

    # Cherche l’état avec l’id = 2
    state = session.query(State).filter(State.id.like(2)).first()

    # Change son nom en "New Mexico"
    state.name = 'New Mexico'

    # Enregistre la modification
    session.commit()

    # Ferme la session
    session.close()
