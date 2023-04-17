#!/usr/bin/python3
""" This module contains the State and Base classes """

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """ The state class inherits from Base """

    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            unique=True)

    name = Column(
            String(128),
            nullable=False)
