#!/usr/bin/python3
""" Task 2 """
from sys import argv
import urllib.request


if __name__ == '__main__':
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
