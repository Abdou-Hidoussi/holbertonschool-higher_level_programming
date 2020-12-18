#!/usr/bin/python3
""" Task 6 """


def find_peak(list_of_integers):
    """ Task 6 """
    if len(list_of_integers) is 0:
        return
    x = list_of_integers.index(max(list_of_integers))
    if (x is not 0) and (x is not len(list_of_integers) - 1):
        return max(list_of_integers)

    list_of_integers.remove(list_of_integers[x])
    return max(list_of_integers)
