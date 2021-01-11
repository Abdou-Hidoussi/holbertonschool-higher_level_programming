#!/usr/bin/python3
""" Task 1 """
from sys import argv
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers["X-Request-Id"])
