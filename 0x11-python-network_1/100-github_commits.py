#!/usr/bin/python3
"""
Python script to access github api and print latest commits
"""

from sys import argv
import requests


def main():
    """
    main function of github scraper
    """

    repo = argv[1]
    owner = argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    resp = requests.get(url).json()

    for commit in resp[:10]:
        if (commit['author']).get('name') is None:
            out = f"{commit['sha']}: {commit['author']['login']}"
            print(out)
        else:
            out = f"{commit['sha']}: {commit['author']['name']}"
            print(out)

if __name__ == '__main__':
    main()
