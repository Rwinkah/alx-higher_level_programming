#!/usr/bin/python3
""" mysqldb project, intro to object relational mappers """


def main():
    """ show all states in state table """
    import argparse
    import MySQLdb
    parser = argparse.ArgumentParser(description='[user] [passwd] [db]')

    parser.add_argument('uname', help="your sql username")
    parser.add_argument('passwd', help="your sql password")
    parser.add_argument('dbase', help="your database name")

    args = parser.parse_args()

    db = MySQLdb.connect(host='localhost', user=args.uname, passwd=args.passwd,
                         port=3306, db=args.dbase)

    curs = db.cursor()

    curs.execute("SELECT * FROM states ORDER BY id")
    records = curs.fetchall()
    for record in records:
        print(record)
    curs.close()
    db.close()


if __name__ == "__main__":
    main()
