#!/usr/bin/python3
""" This module contains a magic class that
    does exactly the same thing as aprticular bytecode """

import dis
class MagicClass:
    """ A magic class """

    def __init__(self, radius=0):
        """ Initialize self """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ Returns the area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Returns the circumference """
        return 2 * math.pi * self.__radius

dis.dis(MagicClass)
