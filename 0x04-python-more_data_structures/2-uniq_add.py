#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    r = 0
    for x in my_list:
        if x not in new:
            new.append(x)
            r += x
    return r
