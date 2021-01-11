#!/usr/bin/python3
""" Task 5 """
from sys import argv
import requests


if __name__ == '__main__':
    html = requests.get(argv[1]).headers["X-Request-Id"]
    print(html)
