#!/usr/bin/python3
"""
    This module contains a class Base that is the base class for
    all subclasses
"""

import json
import csv


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
        if list_objs:
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

        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves instances to a file in csv format """

        attrs = ["id", "size", "width", "height", "x", "y"]
        list_arr = []
        if list_objs:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                row = []
                for attr in attrs:
                    try:
                        row.append(obj_dict[attr])
                    except KeyError:
                        pass
                list_arr.append(row)

        file_name = cls.__name__ + ".csv"
        with open(file_name, "w") as f:
            writer = csv.writer(f, delimiter=",")
            if list_arr:
                for row in list_arr:
                    writer.writerow(row)
            else:
                writer.writerow(["[]"])

    @classmethod
    def load_from_file_csv(cls):
        """ loads instances from a csv file """

        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r") as f:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    field_names = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=field_names)
                list_objs = []
                for row in reader:
                    for attr in field_names:
                        row[attr] = int(row[attr])

                    new_instance = cls.create(**row)
                    list_objs.append(new_instance)
        except FileNotFoundError:
            return []

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


"""
    @staticmethod
    def draw(list_rectangles, list_squares):

        window = turtle.Screen()
        window.bgcolor("white")
        drawer = turtle.Turtle()

        for rect in list_rectangle:
            drawer.color("blue")
            for i in range(2):
                drawer.forward(rect.height)
                drawer.pensize(10)
                drawer.right(rect.width)

        for sqr in list_squares:
            drawer.color("red")
            for i in range(2):
                drawer.forward(sqr.size)
                drawer.pensize(15)
                drawer.right(sqr.width)
"""
