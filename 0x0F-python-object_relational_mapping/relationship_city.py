#!/usr/bin/python3
"""
Module containing the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_base import Base


class City(Base):
    """
    City class.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
