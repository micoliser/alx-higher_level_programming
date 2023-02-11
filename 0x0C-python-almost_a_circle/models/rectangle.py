#!/usr/bin/python3
"""
    This module contains a class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """ A rectangle class that inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes self """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns the width """

        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ returns the height """

        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ returns x """

        return self.__x

    @x.setter
    def x(self, value):
        """ sets x """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ returns y """

        return self.__y

    @y.setter
    def y(self, value):
        """ sets y """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def __str__(self):
        """ calls when instance is printed """

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

        return s

    def area(self):
        """ returns the area of the instance """

        return (self.width * self.height)

    def display(self):
        """ prints the rectangle to stdout """

        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ updates the attribute of the rectangle """

        attr = ["id", "width", "height", "x", "y"]

        if not args:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)
        else:
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
                if i > 4:
                    break

    def to_dictionary(self):
        """ returns the dictionary representation """

        attrs = ["id", "width", "height", "x", "y"]
        dict_r = {}

        for attr in attrs:
            val = getattr(self, attr)
            dict_r[attr] = val

        return dict_r
