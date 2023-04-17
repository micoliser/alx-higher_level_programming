#!/usr/bin/python3\
"""
    This module edits the State object from
    the database hbtn_0e_6_usa with id = 2
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
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

    session.query(State).filter(State.id == 2).update(
            {State.name: "New Mexico"})

    session.commit()
