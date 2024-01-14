#!/usr/bin/python3
""" get states of database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    flag = 0
    for data in session.query(State).order_by(State.id):
        if data.name == sys.argv[4]:
            print(data.id)
            flag = 1

    if flag == 0:
        print("Not found")
