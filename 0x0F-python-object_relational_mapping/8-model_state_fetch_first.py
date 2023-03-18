#!/usr/bin/python3
""" Print the first record in states table """


def main():
    """ query the states table and print the first record """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import State, Base

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format
                           (argv[1], argv[2], argv[3]))
    session = sessionmaker(bind=engine)
    new_session = session()

    states = new_session.query(State)[0]
    if states is not None:
        print(str(states.id) + ":", states.name)


if __name__ == '__main__':
    main()
