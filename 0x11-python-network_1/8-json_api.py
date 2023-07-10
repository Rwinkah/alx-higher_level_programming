#!/usr/bin/python3
"""
Sending post requests with requests module
"""


def main():
    """
    Code wrapped to preven run on import
    """
    import requests as req
    from sys import argv

    if len(argv) < 2:
        q = ''
    else:
        q = argv[1]
    args = {'q': q}

    r = req.post('http://0.0.0.0:5000/search_user', data=args)
    try:
        jsN = r.json()
        if len(jsN) == 0:
            print('No result')
        else:
            print(f"[{jsN['id']}] {jsN['name']}")
    except requests.exceptions:
        print('Not a valid JSON')


if __name__ == '__main__':
    main()
