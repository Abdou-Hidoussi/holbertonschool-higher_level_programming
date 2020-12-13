#!/usr/bin/python3
""" Task 9 """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def Task9():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(asc(State.id)):
        if "a" in instance.name:
            print(str(instance.id) + ': ' + instance.name)
    session.close()

if __name__ == "__main__":
    Task9()
