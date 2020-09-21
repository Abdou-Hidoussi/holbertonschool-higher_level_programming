#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        r = 0
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            r += x
    except:
        pass
    print("")
    return r
