#!/usr/bin/python3
"""Define State class and create database table
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that maps to the states table in the database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}: \
                               {sys.argv[2]}@localhost/{sys.argv[3]}',
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
