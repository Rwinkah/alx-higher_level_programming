#!/usr/bin/python3
"""
Python script using request to hit a url
"""


def main():
    """
    Wrapped in main to prevent run on import
    """
    import requests as req
    r = req.get("https://alx-intranet.hbtn.io/status")
    print('Body response:')
    print(f'\t- type: {type(r.text)}')
    print(f'\t- content: {r.text}')


if __name__ == '__main__':
    main()
