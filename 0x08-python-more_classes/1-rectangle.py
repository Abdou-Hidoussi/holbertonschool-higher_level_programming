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
