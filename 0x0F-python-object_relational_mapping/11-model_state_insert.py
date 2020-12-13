#!/usr/bin/python3
""" Task 11 """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


def Task11():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    item = State(name='Louisiana')
    instance = session.add(item)
    instance = session.query(State).filter(State.name == 'Louisiana').first()
    print(str(instance.id))
    session.commit()
    session.close()

if __name__ == "__main__":
    Task11()
