#!/usr/bin/python3
"""
Python script to manage error messages with urllib
"""


def main():
    """
    Code in main to prevent run on import
    """
    from sys import argv
    from urllib.error import HTTPError
    from urllib.request import Request, urlopen

    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')


if __name__ == '__main__':
    main()
