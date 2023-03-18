#!/usr/bin/python3
""" fetch all states from database """


def main():
    """ fetch all states in a database """

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    new_session = session()

    for state in new_session.query(State):
        print(str(state.id) + ":", state.name)


if __name__ == '__main__':
    main()
