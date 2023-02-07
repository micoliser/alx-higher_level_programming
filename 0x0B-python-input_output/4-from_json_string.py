#!/usr/bin/python3
"""
    This module contains a function that returns the python object
    representation of a JSON string
"""


def from_json_string(my_str):
    """ Returns the python representation of my_obj """

    import json

    return (json.loads(my_str))
