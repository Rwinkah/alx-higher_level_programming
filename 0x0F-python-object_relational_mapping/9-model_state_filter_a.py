#!/usr/bin/python3
""" Find states with a """


def main():
    """ query database for states with a in their name """
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)
    new_session = session()

    a_states = new_session.query(State).order_by(State.id)
    for i in a_states:
        if 'a' in i.name:
            print(str(i.id) + ":", i.name)


if __name__ == '__main__':
    main()
