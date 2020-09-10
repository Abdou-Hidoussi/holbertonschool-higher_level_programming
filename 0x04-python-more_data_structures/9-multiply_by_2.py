#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for x, y in a_dictionary.items():
        new[x] = a_dictionary[x] * 2
    return new
