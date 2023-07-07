#!/usr/bin/python3
"""
Handling error codes with request module
"""


def main():
    """
    Code wrapped to prevent run on import
    """
    import requests as req
    from sys import argv

    r = req.get(argv[1])
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)


if __name__ == '__main__':
    main()
