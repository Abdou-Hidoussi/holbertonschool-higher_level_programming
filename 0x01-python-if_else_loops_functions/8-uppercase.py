#!/usr/bin/python3
def uppercase(str):
    up = list(str)
    for x in range(len(up)):
        if (ord(up[i]) >= ord('a') and ord(up[i]) <= ord('z')):
            up[x] = chr(ord(up[i]) - 32)
    print("{}".format(("").join(up)))
