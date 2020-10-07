#!/usr/bin/python3
"""
task 1
"""


def number_of_lines(filename=""):
    """count line function"""
    x = 0
    with open(filename, encoding="UTF-8") as f:
        for l in f:
            x += 1
    return x
