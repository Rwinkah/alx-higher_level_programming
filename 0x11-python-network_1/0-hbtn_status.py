#!/usr/bin/python3
"""
Python script using urllib package to make a request to alx
"""


def main():

    from urllib.request import urlopen
    req = "https://alx-intranet.hbtn.io/status"

    with urlopen(req) as response:
        resp = response.read()
        print('Body response:')
        print(f"\t- type: {type(resp)}")
        print(f"\t- content: {resp}")
        print(f"\t- utf8 content: {resp.decode('utf8')}")


if __name__ == "__main__":
    main()
