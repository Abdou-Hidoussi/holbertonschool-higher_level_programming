#!/usr/bin/python3
"""Square class
"""


class Square:
    """Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        if not self.__size:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for j in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
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
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
