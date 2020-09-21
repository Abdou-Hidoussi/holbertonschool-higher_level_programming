#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        r = 0
        for i in range(0, x):
            print(my_list[i], end="")
            r += 1
    except (IndexError):
        pass
    print("")
    return r
