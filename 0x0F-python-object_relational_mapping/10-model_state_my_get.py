#!/usr/bin/python3
"""
    This module conatins a script prints the State object from the
    database hbtn_0e_6_usa with name in argv[4]
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
    state_name = sys.argv[4]

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

    state = session.query(State).filter(
            State.name == '{}'.format(state_name)).first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
