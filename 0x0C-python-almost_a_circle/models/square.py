#!/usr/bin/python3
from models.rectangle import Rectangle

""" SQUARE """

class Square(Rectangle):
    """ classs Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = super().width

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self._Rectangle__x, self._Rectangle__y, self.__size))
