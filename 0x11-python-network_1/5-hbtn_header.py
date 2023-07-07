#!/usr/bin/python3
"""
Getting header data with request
"""


def main():
    """
    Code wrapped to prevent run on import
    """
    import requests as req
    from sys import argv

    r = req.get(argv[1])
    print(r.headers['X-Request-Id'])


if __name__ == '__main__':
    main()
