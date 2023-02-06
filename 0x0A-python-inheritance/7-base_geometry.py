#!/usr/bin/python3
"""
    This module contains a BaseGeometry class with a public instance method
    area() that raises an exception and a method integer_validator() that
    validates an integer
"""


class BaseGeometry:
    """
        A BaseGeometry class with public instances area() and
        integer_validator()
    """

    def area(self):
        """ Raises an exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the integer value """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
