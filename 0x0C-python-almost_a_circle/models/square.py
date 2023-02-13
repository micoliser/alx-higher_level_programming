#!/usr/bin/python3
"""
    This module contains a square class inherited from the rectangle
    class

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square class inherited from a rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes self """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ returns size """

        return self.width

    @size.setter
    def size(self, value):
        """ sets size to value """

        self.width = value
        self.height = value

    def __str__(self):
        """ calls when instance is printed """

        s = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

        return s

    def update(self, *args, **kwargs):
        """ updates attributes of the instance """

        attrs = ["id", "size", "x", "y"]

        if not args:
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)
        else:
            i = 0
            for val in args:
                setattr(self, attrs[i], val)
                i += 1
                if i > 3:
                    break

    def to_dictionary(self):
        """ returns the dictionary representation """

        attrs = ["id", "size", "x", "y"]
        dict_r = {}

        for attr in attrs:
            val = getattr(self, attr)
            dict_r[attr] = val

        return dict_r
