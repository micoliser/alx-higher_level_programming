#!/usr/bin/python3
"""
    This module contains a function that creates an object froma json file
"""


def load_from_json_file(filename):
    """ loads a json object from filename """

    import json

    with open(filename, "r", encoding="UTF-8") as f:
        return (json.load(f))
