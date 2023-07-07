#!/usr/bin/python3
"""
python script to send a post request with an argument
"""


def main():
    """
    main script to prevent it from running when imported
    """
    from urllib.request import Request, urlopen
    from sys import argv
    from urllib.parse import urlencode

    em = urlencode({'email': argv[2]})
    data = em.encode('ascii')
    req = Request(argv[1], data)

    with urlopen(req) as resp:
        print(resp.read().decode('utf8'))


if __name__ == '__main__':
    main()
