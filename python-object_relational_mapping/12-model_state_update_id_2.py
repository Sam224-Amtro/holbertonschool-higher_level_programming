#!/usr/bin/python3
"""
Script qui modifie le nom d'un objet State dans la base de données hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    etat_a_modifier = session.query(State).filter_by(id=2).first()
    if etat_a_modifier:
        etat_a_modifier.name = "New Mexico"
        session.commit()
