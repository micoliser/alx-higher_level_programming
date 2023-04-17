#!/usr/bin/python3
""" This module contains the City and Base classes """

from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """ The City class, child of Base married to State """

    __tablename__ = 'cities'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True)

    name = Column(
            String(128),
            nullable=False)

    state_id = Column(
            Integer,
            ForeignKey(State.id),
            nullable=False)
