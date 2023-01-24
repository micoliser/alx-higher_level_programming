#!/usr/bin/python3
""" This module defines a square class with a private size attribute with
    a setter and getter methods to retrieve and update the size attribute.
    Square also has a public instance method area() that gets the
    area of the square and
    my_print() that prints the square with character # to stdout """


class Square:
    """ A square class with a private instance size attribute """

    def __init__(self, size=0):
        """ Initializes self """
        self.__size = size

    @property
    def size(self):
        """ Returns the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size to value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square with character # to stdout """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
