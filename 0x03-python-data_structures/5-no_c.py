#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string[:]
    i = 0
    j = 0
    for x in my_string:
        if x == 'c' or x == 'C':
            new_str = new_str[:(j - i)] + my_string[(j + 1):]
            i += 1
        j += 1
    return new_str
