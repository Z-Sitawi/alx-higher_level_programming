#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base():
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column

Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
