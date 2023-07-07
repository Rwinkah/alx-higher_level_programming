#!/usr/bin/python3
"""
using request to get the X-Request-Id
"""


def main():
    """
    main program using python urllib
    """
    from sys import argv
    from urllib.request import urlopen, Request

    url = argv[1]

    req = Request(url)

    with urlopen(req) as response:
        print(response.headers['X-Request-Id'])


if __name__ == '__main__':
    main()
