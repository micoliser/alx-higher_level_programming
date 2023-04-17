#!/usr/bin/python3
"""
    This module lists all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    driver = "mysql+mysqldb"
    uname = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
            '{}://{}:{}@localhost:3306/{}'.format(
                driver,
                uname,
                password,
                dbname))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_city = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all()

    for state, city in state_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
