#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string[:]
    i = 0
    for x in my_string:
        if my_string[x] == 'c' or my_string[x] == 'C':
            new_str = new_str[:(x - i)] + my_string[(x + 1):]
            i++
    return new_str
