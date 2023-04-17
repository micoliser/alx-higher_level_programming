#!/usr/bin/python3
"""
    This module ists all City objects, contained in the
    database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    import sys
    from relationship_state import State
    from relationship_city import City
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
                dbname),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id)

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
