#!/usr/bin/python3
"""
Defines the State class and an instance Base = declarative_base()
to work with SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the Base instance
Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database."""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
