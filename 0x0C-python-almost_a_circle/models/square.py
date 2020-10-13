#!/usr/bin/python3
""" SQUARE """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ classs Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        string1 = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        string2 = "{}/{} ".format(self.x, self.y)
        string3 = "- {}".format(self.width)
        return(string1 + string2 + string3)

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
        self.__size = value