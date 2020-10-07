#!/usr/bin/python3
"""
task 2
"""


def read_lines(filename="", nb_lines=0):
    """read line function"""
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return
        for i in range(nb_lines):
            print(f.readline(), end="")
