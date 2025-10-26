#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create the engine and connect to the database
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object and add it to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
