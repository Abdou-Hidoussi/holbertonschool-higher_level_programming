#!/usr/bin/python3
"""
task 12
"""


class MyInt(int):
    """ My inherit class """
    def __init__(self, value):
        self.value = value

    def __ne__(self, comp):
        return (self.value == comp)

    def __eq__(self, comp):
        return self.value != comp
