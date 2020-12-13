#!/usr/bin/python3
""" Task 10 """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def Task10():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == argv[4]).first()
    if instance is not None:
        print(str(instance.id))
    else:
        print("Not found")
    session.close()

if __name__ == "__main__":
    Task10()
