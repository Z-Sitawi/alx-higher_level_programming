#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for state in states:
        print(state)
    session.close()