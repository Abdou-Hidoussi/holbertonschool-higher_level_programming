#!/usr/bin/python3
"""
task 10
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ My inherit class """
    def __init__(self, size):
        self.integer_validator("size", size)
        super(Rectangle, self).__init__()
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        return self.__size ** 2
