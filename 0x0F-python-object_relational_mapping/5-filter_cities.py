#!/usr/bin/python3
""" Finding a particular state in state table """


def main():
    """ Using mysqldb to check for a state in state table """
    import argparse
    import MySQLdb

    parser = argparse.ArgumentParser(description="search for a state")
    parser.add_argument('usr', help="specify user name")
    parser.add_argument('pwd', help="specify login pwd")
    parser.add_argument('dbase', help="specify database name")
    parser.add_argument('search', help="specify state for search")

    args = parser.parse_args()

    db = MySQLdb.connect(host='localhost', port=3306, user=args.usr,
                         passwd=args.pwd, db=args.dbase)
    curs = db.cursor()
    city = args.search
    curs.execute("SELECT cities.name FROM cities INNER JOIN states ON \
                 cities.state_id = states.id WHERE states.name \
                 = %s", (args.search,))
    row = curs.fetchall()
    for rows in row:
        print("{}".format(rows[0]), end='')
        if rows != row[-1]:
            print(", ", end='')
    print("")
    curs.close()
    db.close()


if __name__ == '__main__':
    main()
