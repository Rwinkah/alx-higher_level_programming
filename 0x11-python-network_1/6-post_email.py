#!/usr/bin/python3
"""
Sending data using post in requests lib
"""


def main():
    """
    Code wrapped to prevent run on import
    """
    import requests as req
    from sys import argv

    args = {'email': argv[2]}

    r = req.post(argv[1], data=args)
    print(r.text)


if __name__ == '__main__':
    main()
