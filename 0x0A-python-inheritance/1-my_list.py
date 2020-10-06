#!/usr/bin/python3
"""
Task 2
"""


class MyList(list):
    """ My inherited class """

    def print_sorted(self):
        return print(sorted(self))
