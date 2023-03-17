#!/usr/bin/python3
""" selecting states that begin with capital N """


def main():
    """ select states that begin with N"""
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
    curs.execute("SELECT * FROM states")
    records = curs.fetchall()
    [print(row) for row in records if row[1][0] == 'N']
    curs.close()
    db.close()


if __name__ == '__main__':
    main()
