#!/usr/bin/python3
""" This module defines a square class with a private size attribute.
    Square also has a public instance method area() that gets the area
    of the square """


class Square:
    """ A square class with a private instance size attribute """

    def __init__(self, size=0):
        """ Initializes self """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size
