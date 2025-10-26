#!/usr/bin/python3
"""
Defines a state class and an instance of base using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Créer l'instance de base
Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table "states".
    """
    __tablename__= "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
