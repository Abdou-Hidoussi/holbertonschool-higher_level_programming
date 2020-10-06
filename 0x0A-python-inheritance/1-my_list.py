#!/usr/bin/python3
class MyList(list):
    """ My inherited class """

    def print_sorted(self):
        return print(sorted(self))
