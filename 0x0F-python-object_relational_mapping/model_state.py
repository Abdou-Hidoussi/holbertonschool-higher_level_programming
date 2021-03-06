#!/usr/bin/python3
""" Task 6 """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ class task 6 """
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
