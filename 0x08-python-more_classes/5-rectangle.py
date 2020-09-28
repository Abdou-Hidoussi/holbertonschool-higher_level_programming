#!/usr/bin/python3
"""empty rectangle class
"""


class Rectangle:
    """empty rectangle class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
            return
        if value < 0:
            raise ValueError("width must be >= 0")
            return
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
            return
        if value < 0:
            raise ValueError("height must be >= 0")
            return
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return rec
        for x in range(self.__height):
            for y in range(self.__width):
                rec += "#"
            rec += '\n'
        return rec[:-1]

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
