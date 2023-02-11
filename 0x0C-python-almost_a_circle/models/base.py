#!/usr/bin/python3
"""
    This module contains a class Base that is the base class for
    all subclasses
"""

import json


class Base:
    """ The base class with id instance attributes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes self """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON representation of list_objs to a file """

        list_dict = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            list_dict.append(obj_dict)

        json_string = Base.to_json_string(list_dict)
        file_name = cls.__name__ + ".json"

        with open(file_name, "w") as f:
            f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """

        new = cls(1, 1)
        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances loaded from a file """

        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []
        else:
            list_dict = Base.from_json_string(json_string)

        list_objs = []
        for obj_dict in list_dict:
            new_instance = cls.create(**obj_dict)
            list_objs.append(new_instance)

        return list_objs

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON representation of list_dictionaries """

        if not list_dictionaries:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of a JSON representation json_string """

        if not json_string:
            return []
        else:
            return json.loads(json_string)
