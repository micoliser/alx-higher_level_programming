#!/usr/bin/python3
"""
    This Module contains a lookup function thar returns all the available
    attributes and methods of an object
"""


def lookup(obj):
    """ Returns the attributes and methods of an object """

    return (dir(obj))
