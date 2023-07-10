#!/usr/bin/python3
"""
Module to check for git id
"""


def main():
    """
    Code wrapped to prevent run on import
    """
    from sys import argv
    import requests as req
    from requests.auth import HTTPBasicAuth as httpAuth

    password = argv[2]
    username = argv[1]

    auth = httpAuth(username, password)

    r = req.post('https://api.github.com/users', auth=auth)
    if r.status_code == 200:
        try:
            resp = r.json()
            print(r.json()['id'])
        except ValueError:
            print('None')
    else:
        print('None')


if __name__ == '__main__':
    main()

print(self.__doc__)
