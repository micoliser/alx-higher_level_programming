import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """ class to test the Base class """

    def setUp(self):
        """ calls before each test """

        Base._Base__nb_objects = 0

    def test_base_id(self):
        """ test the base class """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(5)
        self.assertEqual(b2.id, 5)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b5 = Base(None)
        self.assertEqual(b5.id, 3)
        b6 = Base(-10)
        self.assertEqual(b6.id, -10)
        b7 = Base(0)
        self.assertEqual(b7.id, 0)

    def test_base_id_string(self):
        """ test base id with strings """

        b1 = Base("3")
        self.assertEqual(b1.id, "3")
        b2 = Base("1")
        self.assertEqual(b2.id, "1")

    def test_base_id_more_args(self):
        """ test id with more args than expected """

        with self.assertRaises(TypeError):
            b1 = Base(1, 4)

    def test_base_to_json_string(self):
        """ test the to_json_string """

        list_dict = [
            {"id": 1, "height": 5, "width": 4, "x": 0, "y": 0},
            {"id": 2, "height": 15, "width": 5, "x": 2, "y": 0},
            {"id": 3, "height": 5, "width": 4, "x": 4, "y": 2}
        ]

        base_json = Base.to_json_string(list_dict)
        self.assertTrue(type(base_json) is str)
        self.assertEqual(base_json, json.dumps(list_dict))

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")

    def test_base_to_json_string2(self):
        """ test the to_json_string with instances """

        r1 = Rectangle(2, 4)
        r1_list = [r1.to_dictionary()]

        r1_base_json = Base.to_json_string(r1_list)
        self.assertTrue(type(r1_base_json) is str)
        self.assertEqual(r1_base_json, json.dumps(r1_list))

        s1 = Square(4)
        s1_list = [s1.to_dictionary()]

        s1_base_json = Base.to_json_string(s1_list)
        self.assertTrue(type(s1_base_json) is str)
        self.assertTrue(s1_base_json, json.dumps(r1_list))

    def test_base_to_json_string_more_args(self):
        """ test the to_json_string with more args than expected """

        r1 = Rectangle(5, 4)
        s1 = Square(5)

        with self.assertRaises(TypeError):
            Base.to_json_string([r1.to_dictionary()], [s1.to_dictionary()])

    def test_base_to_json_string_no_args(self):
        """ test the to_json_string with no args """

        r1 = Rectangle(5, 4)
        s1 = Square(5)

        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_base_from_json_string(self):
        """ test the from_json_string """

        list_dict = [
            {"id": 1, "height": 5, "width": 4, "x": 0, "y": 0},
            {"id": 2, "height": 15, "width": 5, "x": 2, "y": 0},
            {"id": 3, "height": 5, "width": 4, "x": 4, "y": 2}
        ]

        base_json = Base.to_json_string(list_dict)
        output = Base.from_json_string(base_json)
        self.assertFalse(type(output) is str)
        self.assertTrue(type(output) is list)
        self.assertEqual(output, json.loads(base_json))

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{}]"), [{}])

    def test_base_from_json_string2(self):
        """ test the from_json_string with instances """

        r1 = Rectangle(2, 4)
        r1_list = [r1.to_dictionary()]

        r1_base_json = Base.to_json_string(r1_list)
        output = Base.from_json_string(r1_base_json)
        self.assertTrue(type(output) is list)
        self.assertEqual(output, json.loads(r1_base_json))

        s1 = Square(4)
        s1_list = [s1.to_dictionary()]

        s1_base_json = Base.to_json_string(s1_list)
        output = Base.from_json_string(s1_base_json)
        self.assertTrue(type(output) is list)
        self.assertEqual(output, json.loads(s1_base_json))

    def test_base_from_json_string_more_args(self):
        """ test the from_json_string with more args than expected """

        r1 = Rectangle(5, 4)
        s1 = Square(5)

        with self.assertRaises(TypeError):
            Base.from_json_string([r1.to_dictionary()], [s1.to_dictionary()])

    def test_base_from_json_string_no_args(self):
        """ test the from_json_string with no args """

        r1 = Rectangle(5, 4)
        s1 = Square(5)

        with self.assertRaises(TypeError):
            Base.to_json_string()
