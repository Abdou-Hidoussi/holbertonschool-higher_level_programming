#!/usr/bin/python3
from models.base import Base
""" RECTANGLE """


class Rectangle(Base):
    """ classs RECTANGLE
    """
    def __init__(self, width, height, x=0, y=0, id=None):
    """ __init__ function
    """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
    """ width function
    """
        return self.__width

    @width.setter
    def width(self, value):
    """ width function
    """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
    """ height function
    """
        return self.__hight

    @height.setter
    def height(self, value):
    """ height function
    """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
    """ x function
    """
        return self.__x

    @x.setter
    def x(self, value):
    """ x function
    """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
    """ y function
    """
        return self.__y

    @y.setter
    def y(self, value):
    """ y function
    """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
    """ area function
    """
        return (self.__height * self.__width)

    def display(self):
    """ display function
    """
        if self.__height == 0 or self.__width == 0:
            print("")
        else:
            for i in range(self.__x):
                print("")
            for j in range(0, self.__width):
                for k in range(self.__y):
                    print(" ", end='')
                for l in range(self.__height):
                    print("#", end='')
                print("")

    def __str__(self):
    """ __str__ function
    """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
    """ update function
    """
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            if len(args) > 0:
                setattr(self, "id", args[0])
            if len(args) > 1:
                setattr(self, "width", args[1])
            if len(args) > 2:
                setattr(self, "height", args[2])
            if len(args) > 3:
                setattr(self, "x", args[3])
            if len(args) > 4:
                setattr(self, "y", args[4])
