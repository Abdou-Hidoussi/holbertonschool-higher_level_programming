#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = len(sys.argv) - 1

    if argument == 0:
        print("{:d} arguments.".format(argument))
    elif argument == 1:
        print("{:d} argument:".format(argument))
    else:
        print("{:d} arguments:".format(argument))

    if argument > 0:
        count = 0
        for x in sys.argv[1:]:
            count += 1
            print("{:d}: {:s}".format(count, x))
