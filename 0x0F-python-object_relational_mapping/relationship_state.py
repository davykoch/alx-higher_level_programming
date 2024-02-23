#!/usr/bin/python3
"""
Module containing the State class with a relationship with the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_base import Base
from relationship_city import City


class State(Base):
    """
    State class with a relationship with the City class.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)

    cities = (relationship
              ("City", backref="state", cascade="all, delete-orphan"))
