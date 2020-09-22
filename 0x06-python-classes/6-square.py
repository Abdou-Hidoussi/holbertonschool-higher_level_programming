#!/usr/bin/python3
"""Square class
"""


class Square:
    """Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        if not self.__size:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(0, self.__size):
                for x in range(self.__position[0]):
                    print(" ", end='')
                for y in range(self.__size):
                    print("#", end='')
                print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or not isinstance(value, tuple) or\
           not isinstance(value[0], int) or value[0] < 0 or\
           not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
