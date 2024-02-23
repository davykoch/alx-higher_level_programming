#!/usr/bin/python3
"""
Script that lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = (session.query(State, City)
              .filter(State.id == City.state_id)
              .order_by(State.id, City.id))

    for state, city in result:
        if not hasattr(state, 'printed'):
            print(f"{state.id}: {state.name}")
            setattr(state, 'printed', True)
        print(f"    {city.id}: {city.name}")

    session.close()
