#!/usr/bin/python3
"""
task 0
"""


def read_file(filename=""):
    with open(filename, encoding="UTF-8") as f:
        str = f.read()
        print(str, end="")
