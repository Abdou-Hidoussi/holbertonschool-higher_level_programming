#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summ = 0
    for x in sys.argv[1:]:
        summ += int(x)
    print(summ)
