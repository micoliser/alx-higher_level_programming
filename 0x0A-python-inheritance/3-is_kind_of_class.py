#!/usr/bin/python3
"""
    This module contains a function that checks if an object is an instance
    of, or if the object is an instance of a class that inherits from
    the specified class
"""


def is_kind_of_class(obj, a_class):
    """ Checks if an object is kind of a class """

    return (isinstance(obj, a_class))
