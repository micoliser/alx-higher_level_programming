#!/usr/bin/python3
"""
    This module contains a BaseGeometry class with a public instance method
    area() that raises an exception
"""


class BaseGeometry:
    """ A BaseGeometry class with public instance method area()"""

    def area(self):
        """ Raises an exception """

        raise Exception("area() is not implemented")
