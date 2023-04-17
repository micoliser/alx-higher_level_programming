#!/usr/bin/python3
"""
    Creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa
"""

if __name__ == "__main__":
    import sys
    from relationship_state import State
    from relationship_city import Base, City
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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new = City(name="San Francisco", state=State(name="California"))

    session.add(new)
    session.commit()
