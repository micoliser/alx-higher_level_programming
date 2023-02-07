#!/usr/bin/python3
"""
    This module contains a functionthat returns the dictionary
    description of an object with simple data structure
"""


def class_to_json(obj):
    """
        A function that returns a dictionary description of
        an object
    """

    return (obj.__dict__)
