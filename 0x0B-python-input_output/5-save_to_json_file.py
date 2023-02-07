#!/usr/bin/python3
"""
    This module contains a function that writes an object to a text file using
    a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """ saves my_obj as a json representation to filename """

    import json

    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
