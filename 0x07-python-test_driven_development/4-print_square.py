
#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
        return

    if size < 0:
        raise ValueError('size must be >= 0')
        return

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print("")
