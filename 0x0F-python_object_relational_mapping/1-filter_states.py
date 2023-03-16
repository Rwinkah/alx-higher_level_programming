#!/usr/bin/python3
""" selecting states that begin with capital N """


def main():
    import argparse
    import MySQLdb

    parser = argparse.ArgumentParser(description='get arguments')
    parser.add_argument('uname', help='username for login')
    parser.add_argument('passwd', help='passwd for login')
    parser.add_argument('dbase', help='database name')

    args = parser.parse_args()

    db = MySQLdb.connect(host='localhost', user=args.uname, passwd=args.passwd,
                         port=3306, db=args.dbase)

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    records = curs.fetchall()
    for row in records:
        print(row)
    curs.close()
    db.close()


if __name__ == '__main__':
    main()
