#!/usr/bin/python3
""" Task 8 """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def Task8():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).order_by(asc(State.id)).first()
    if instance is not None:
        print(str(instance.id) + ': ' + instance.name)
    else:
        print("Nothing")
    session.close()

if __name__ == "__main__":
    Task8()
