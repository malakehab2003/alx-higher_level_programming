#!/usr/bin/python3
"""Create State "California" with City "San Francisco" from database"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for data in session.query(State).order_by(State.id):
        print(f"{data.id}: {data.name}")
        for city in data.cities:
            print("    ", end="")
            print(f"{city.id}: {city.name}")
