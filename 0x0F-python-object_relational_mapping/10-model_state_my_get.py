#!/usr/bin/python3
""" finding states in database table """


def main():
    """ Check for a record in states table """
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)
    new_session = session()

    find_state = new_session.query(State).filter(State.name == argv[4])
    if len(list(find_state)) == 0:
        print('Not found')
        return
    for i in find_state:
        print(i.name)
        print(i.id)


if __name__ == '__main__':
    main()
