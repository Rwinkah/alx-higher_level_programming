#!/usr/bin/python3
""" Selecting all cities from a table """


def main():
    """ list all cities in cities table"""
    import argparse
    import MySQLdb as ms

    parser = argparse.ArgumentParser(description="finding cities in db")
    parser.add_argument('uname', help="specify username")
    parser.add_argument('pwd', help="specify password")
    parser.add_argument('dbase', help="dbase name")

    args = parser.parse_args()
    db = ms.connect(host='localhost', user=args.uname, port=3306,
                    passwd=args.pwd, db=args.dbase)
    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM cities  \
                 INNER JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id")
    records = curs.fetchall()
    for row in records:
        print(row)
    curs.close()
    db.close()


if __name__ == '__main__':
    main()
