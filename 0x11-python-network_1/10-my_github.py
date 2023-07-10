#!/usr/bin/python3
"""
my_github

Module to access github api and return id number.
"""


def main():
    """
    Code wrapped to prevent run on import.
    """
    import requests as req
    from sys import argv
    from requests.auth import HTTPBasicAuth as httpAuth

    username = argv[1]
    password = argv[2]
    authe = httpAuth(username, password)

    r = req.get('https://api.github.com/users', auth=authe)
    if r.status_code == 200:
        try:
            response = r.json()
            print(response)
        except ValueError:
            print('None')
    else:
        print('None')


if __name__ == '__main__':
    main()
