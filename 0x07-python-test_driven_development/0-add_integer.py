#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
        return
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
        return
    return int(a) + int(b)
