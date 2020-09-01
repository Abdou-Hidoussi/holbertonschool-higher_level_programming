#!/usr/bin/python3
for x in range(97, 123):
    if not(x == 101 or x == 113):
        print("{:c}".format(x), end='')
