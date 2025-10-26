#!/usr/bin/python3
"""
Ajoute l'objet State "Louisiana" à la base de données hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Crée le moteur et se connecte à la base de données
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Création d'une classe « Session » configurée
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crée un nouvel objet State et l'ajoute à la base de données
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Affiche l'id du nouvel état
    print(new_state.id)

    # Ferme la session
    session.close()
