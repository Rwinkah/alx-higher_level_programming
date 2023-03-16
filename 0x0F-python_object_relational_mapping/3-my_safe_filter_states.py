#!/usr/bin/python3
""" Finding a particular state in state table """


def main():
    """
    Using mysqldb to check for a state in state table
    while escaping strings to avoid sql injection
    """
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
    state_name = args.search
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name = ?", (state_name,))
    row = curs.fetchone()
    print(row)
    curs.close()
    db.close()


if __name__ == '__main__':
    main()
