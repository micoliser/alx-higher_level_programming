#!/usr/bin/python3
"""
    This module contains a function that checks if an object is an instance
    of a class that inherited (directly or indirectly) from a specified class
"""


def inherits_from(obj, a_class):
    """ Checks if an object inherits from a class directly or indirectly"""

    if type(obj) is a_class:
        return False
    return (isinstance(obj, a_class))
