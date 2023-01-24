#!/usr/bin/python3
""" This module defines a square class with a private size attribute """


class Square:
    """ A square class with a private instance size attribute """

    def __init__(self, size=0):
        """ Initializes self """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
