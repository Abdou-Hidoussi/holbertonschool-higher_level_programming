#!/usr/bin/python3
""" SQUARE """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ __str__ """
        return"[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ update """
        keys = ['id', 'size', 'x', 'y']
        if args:
            for key, value in zip(keys, args):
                setattr(self, key, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ to_dictionary """
        dic = {'id': self.id, 'x': self.x, 'y': self.y,
               'size': self.size}
        return dic
