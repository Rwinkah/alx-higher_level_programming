#!/usr/bin/python3
""" Interacting with databases through sqlalchemy ORM """
from sqlalchemy import, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ Class definition of state table """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
