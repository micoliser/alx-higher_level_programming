#!/usr/bin/python3
""" This module contains the City and Base classes """

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


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
            ForeignKey("states.id"),
            nullable=False)
