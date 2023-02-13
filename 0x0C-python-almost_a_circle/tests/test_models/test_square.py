import unittest
import io
import sys
import json
from pathlib import Path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ class to test the square class """

    def setUp(self):
        """ set up base """

        Base._Base__nb_objects = 0

    def test_square(self):
        """ test the sqaure """

        s1 = Square(5, 1, 2, 3)

        self.assertEqual(s1.id, 3)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)

    def test_square2(self):
        """ test the square """

        s1 = Square(1, 1)

        s1.id = 2
        self.assertEqual(s1.id, 2)
        s1.size = 5
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        s1.x = 3
        self.assertEqual(s1.x, 3)
        s1.y = 1
        self.assertEqual(s1.y, 1)

    def test_square_no_id(self):
        """ test square without id """

        s1 = Square(7, 2, 5)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 5)

    def test_square_no_y(self):
        """ test square without y """

        s1 = Square(3, 2)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)

    def test_square_invalid_y1(self):
        """ test square with wrong y value """

        s1 = Square(5, 2, 3, 4)

        with self.assertRaises(TypeError):
            s2 = Square(6, 1, "10")
        with self.assertRaises(TypeError):
            s3 = Square(6, 1, True)
        with self.assertRaises(TypeError):
            s4 = Square(6, 1, [1, 2])
        with self.assertRaises(TypeError):
            s5 = Square(6, 1, (1, 1))
        with self.assertRaises(TypeError):
            s6 = Square(6, 1, {"z", 10})
        with self.assertRaises(TypeError):
            s1.y = False
        with self.assertRaises(TypeError):
            s1.y = "hello"
        with self.assertRaises(TypeError):
            s1.y = [2, 5]
        with self.assertRaises(TypeError):
            s1.y = (1, 16)

    def test_square_invalid_y2(self):
        """ test square with wrong y """

        s1 = Square(1, 3, 2, 0)

        with self.assertRaises(ValueError):
            s2 = Square(1, 2, -17)
        with self.assertRaises(ValueError):
            s3 = Square(1, 2, -1, 12)
        with self.assertRaises(ValueError):
            s1.y = -1
        with self.assertRaises(ValueError):
            s1.y = -25

    def test_square_no_x(self):
        """ test square without x """

        s1 = Square(4)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_invalid_x1(self):
        """ test square with wrong x value """

        s1 = Square(5, 2, 3, 4)

        with self.assertRaises(TypeError):
            s2 = Square(6, "10", 5)
        with self.assertRaises(TypeError):
            s3 = Square(6, True, 0, 2)
        with self.assertRaises(TypeError):
            s4 = Square(6, [1, 2], 1)
        with self.assertRaises(TypeError):
            s5 = Square(6, (1, 1), 0, 0)
        with self.assertRaises(TypeError):
            s6 = Square(6, {"z", 10}, 12)
        with self.assertRaises(TypeError):
            s1.x = False
        with self.assertRaises(TypeError):
            s1.x = "hello"
        with self.assertRaises(TypeError):
            s1.x = [2, 5]
        with self.assertRaises(TypeError):
            s1.x = (1, 16)

    def test_square_invalid_x2(self):
        """ test square with wrong x """

        s1 = Square(1, 3, 2, 0)

        with self.assertRaises(ValueError):
            s2 = Square(1, -17, 12)
        with self.assertRaises(ValueError):
            s3 = Square(1, -1, 0, 1)
        with self.assertRaises(ValueError):
            s1.x = -1
        with self.assertRaises(ValueError):
            s1.x = -25

    def test_square_no_size(self):
        """ test square without size """

        with self.assertRaises(TypeError):
            s1 = Square()

    def test_square_invalid_size1(self):
        """ test square with wrong size """

        s1 = Square(5, 2, 3, 4)

        with self.assertRaises(TypeError):
            s2 = Square("10", 5, 2, 1)
        with self.assertRaises(TypeError):
            s3 = Square(True, 0, 2)
        with self.assertRaises(TypeError):
            s4 = Square([1, 2], 1)
        with self.assertRaises(TypeError):
            s5 = Square((1, 1), 0, 0)
        with self.assertRaises(TypeError):
            s6 = Square({"z", 10}, 12)
        with self.assertRaises(TypeError):
            s1.size = False
        with self.assertRaises(TypeError):
            s1.size = "hello"
        with self.assertRaises(TypeError):
            s1.size = [2, 5]
        with self.assertRaises(TypeError):
            s1.size = (1, 16)

    def test_square_invalid_size2(self):
        """ test square with wrong size """

        s1 = Square(1, 3, 2, 0)

        with self.assertRaises(ValueError):
            s2 = Square(-17, 12)
        with self.assertRaises(ValueError):
            s3 = Square(-1, 0, 1)
        with self.assertRaises(ValueError):
            s4 = Square(0, 2, 1, 5)
        with self.assertRaises(ValueError):
            s1.size = -50
        with self.assertRaises(ValueError):
            s1.size = 0

    def test_square_more_args(self):
        """ test square with more args than expected """

        with self.assertRaises(TypeError):
            s1 = Square(1, 3, 4, 0, 12)

    def test_square_area(self):
        """ test square area """

        s1 = Square(10)
        self.assertEqual(s1.area(), 100)

        s1.size = 5
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 5, 10)
        self.assertEqual(s2.area(), 4)

        s3 = Square(17, 2, 2, 0)
        self.assertEqual(s3.area(), 289)

        s4 = Square(1)
        self.assertEqual(s4.area(), 1)

        s4.size = 15
        self.assertEqual(s4.area(), 225)

    def test_square_area_args(self):
        """ test square area with args """

        s1 = Square(17, 2)

        with self.assertRaises(TypeError):
            s1.area(14)

    def test_square_str(self):
        """ test the square__str__ method """

        s1 = Square(4, 2, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/2 - 4")

        s2 = Square(12)
        self.assertEqual(s2.__str__(), "[Square] (2) 0/0 - 12")

        s3 = Square(5, 1, 2, 10)
        self.assertEqual(s3.__str__(), "[Square] (10) 1/2 - 5")

    def test_square_str_args(self):
        """ test square __str__ method with args """
        s1 = Square(13)

        with self.assertRaises(TypeError):
            s1.__str__("hey")

    def test_square_display(self):
        """ test the display method """

        s1 = Square(4)
        output = io.StringIO()
        sys.stdout = output
        s1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "####\n####\n####\n####\n")

    def test_square_display2(self):
        """ test the display method """

        s1 = Square(3, 2, 1)
        output = io.StringIO()
        sys.stdout = output
        s1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "\n  ###\n  ###\n  ###\n")

    def test_square_display3(self):
        """ test the display method """

        s1 = Square(2, 2)
        output = io.StringIO()
        sys.stdout = output
        s1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "  ##\n  ##\n")

    def test_square_display4(self):
        """ test the display method """

        s1 = Square(4, 0, 3)
        output = io.StringIO()
        sys.stdout = output
        s1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "\n\n\n####\n####\n####\n####\n")

    def test_square_display_args(self):
        """ test display with args """

        s1 = Square(4)

        with self.assertRaises(TypeError):
            s1.display("hello")

    def test_square_update_args(self):
        """ test the square update method """

        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)

        s1.update(2)
        self.assertEqual(s1.id, 2)

        s1.update(10, 5, 3)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 10)

        s1.update(4, 1, 4, 5)
        self.assertEqual(s1.id, 4)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)

        # update with extra values in args
        s1.update(15, 10, 5, 2, 22, 12, 22)
        self.assertEqual(s1.id, 15)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 2)

        # if args and kwargs is given, args is used
        s1.update(1, 20, 8, 2, size=1, id=5, x=2, y=4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.width, 20)
        self.assertEqual(s1.height, 20)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 2)

    def test_square_update_invalid_args1(self):
        """ test square update with invalid args """

        s1 = Square(16)

        # size errors
        with self.assertRaises(TypeError):
            s1.update(1, "s", 1)
        with self.assertRaises(TypeError):
            s1.update(2, True, 15)
        with self.assertRaises(TypeError):
            s1.update(1, [1])
        with self.assertRaises(TypeError):
            s1.update(2, {"y": 15})
        with self.assertRaises(TypeError):
            s1.update(1, (1, 2), 25)

        # x errors
        with self.assertRaises(TypeError):
            s1.update(12, 20, "13")
        with self.assertRaises(TypeError):
            s1.update(1, 5, False)
        with self.assertRaises(TypeError):
            s1.update(2, 15, [1])
        with self.assertRaises(TypeError):
            s1.update(3, 20, {"y": 15}, 25)

        # y errors
        with self.assertRaises(TypeError):
            s1.update(1, 15, 0, "13")
        with self.assertRaises(TypeError):
            s1.update(2, 2, 12, True)
        with self.assertRaises(TypeError):
            s1.update(3, 17, 1, [1, 2])
        with self.assertRaises(TypeError):
            s1.update(4, 20, 2, {"y": 15}, 25)

    def test_square_update_invalid_args2(self):
        """ test square update with invalid args """

        s1 = Square(16)

        # size errors
        with self.assertRaises(ValueError):
            s1.update(1, -5, 1)
        with self.assertRaises(ValueError):
            s1.update(1, 0)

        # x errors
        with self.assertRaises(ValueError):
            s1.update(12, 20, -17)

        # y errors
        with self.assertRaises(ValueError):
            s1.update(2, 1, 0, -20)

    def test_square_update_kwargs(self):
        """ test square update with kwargs """

        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)

        s1.update(id=2, size=5)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        s1.update(y=2, x=5)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 2)

        s1.update(size=13, y=5, x=17, id=2)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 13)
        self.assertEqual(s1.width, 13)
        self.assertEqual(s1.height, 13)
        self.assertEqual(s1.x, 17)
        self.assertEqual(s1.y, 5)

    def test_square_update_invalid_kwargs1(self):
        """ test square update with invalid kwargs """

        s1 = Square(16)
        invalid_t = ["1", (1, 2), True, False, "65", [1], {"w": 5}]

        # size errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                s1.update(size=typ, id=1)

        # x errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                s1.update(x=typ, size=15)

        # y errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                s1.update(x=0, y=typ)

    def test_square_update_invalid_kwargs2(self):
        """ test square update with invalid kwargs """

        s1 = Square(16)

        # size errors
        with self.assertRaises(ValueError):
            s1.update(size=-5)
        with self.assertRaises(ValueError):
            s1.update(size=0, id=3)

        # x errors
        with self.assertRaises(ValueError):
            s1.update(id=5, x=-17)

        # y errors
        with self.assertRaises(ValueError):
            s1.update(y=-20)

    def test_square_update_less_args(self):
        """ test square update method with less args """

        s1 = Square(12)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.width, 12)
        self.assertEqual(s1.height, 12)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        # when update is called with no args, rect does not change
        s1.update()

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.width, 12)
        self.assertEqual(s1.height, 12)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_to_dictionary(self):
        """ test the to_dictionary method """

        s1 = Square(5, 2, 1, 2)
        dict_s1 = s1.to_dictionary()
        self.assertEqual(dict_s1["id"], 2)
        self.assertEqual(dict_s1["x"], 2)
        self.assertEqual(dict_s1["y"], 1)
        self.assertEqual(dict_s1["size"], 5)

        s1.update(1, 7, 4)
        dict_s1 = s1.to_dictionary()
        self.assertEqual(dict_s1["id"], 1)
        self.assertEqual(dict_s1["x"], 4)
        self.assertEqual(dict_s1["y"], 1)
        self.assertEqual(dict_s1["size"], 7)

    def test_square_to_dictionary_err(self):
        """ test to_dictionary with error """

        s1 = Square(15)
        dict_s1 = s1.to_dictionary()

        with self.assertRaises(KeyError):
            dict_s1["height"]
        with self.assertRaises(KeyError):
            dict_s1["width"]

    def test_suqare_to_dictionary_args(self):
        """ test to_dictionary method with args """

        s1 = Square(10)

        with self.assertRaises(TypeError):
            dict_s1 = s1.to_dictionary("hey")

    def test_square_save_to_file(self):
        """ test the save to file method """

        s1 = Square(6)
        s2 = Square(4, 1, 3, 1)
        Square.save_to_file([s1, s2])

        sqr_file = Path("Square.json")
        self.assertTrue(sqr_file.is_file())

        sqr_list = [s1.to_dictionary(), s2.to_dictionary()]
        with open(sqr_file, "r") as f:
            self.assertEqual(f.read(), json.dumps(sqr_list))

    def test_square_save_to_file2(self):
        """ test the save to file method """

        s1 = Square(5, 3, 1)
        Square.save_to_file([s1])

        sqr_file = Path("Square.json")
        self.assertTrue(sqr_file.is_file())

        with open(sqr_file, "r") as f:
            self.assertEqual(f.read(), json.dumps([s1.to_dictionary()]))

    def test_square_save_to_file3(self):
        """ test the save to file method """

        s1 = Square(2)
        s2 = Square(2, 4, 1, 1)
        s3 = Square(4, 1, 2)
        Square.save_to_file([s1, s2, s3])

        sqr_file = Path("Square.json")
        self.assertTrue(sqr_file.is_file())

        sqr_list = [s1.to_dictionary(), s2.to_dictionary(), s3.to_dictionary()]
        with open(sqr_file, "r") as f:
            self.assertEqual(f.read(), json.dumps(sqr_list))

    def test_square_save_to_file_none(self):
        """ test the save to file method with none """

        Square.save_to_file(None)

        sqr_file = Path("Square.json")
        self.assertTrue(sqr_file.is_file())

        with open(sqr_file, "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_more_args(self):
        """  test save to file with more args than expected """

        s1 = Square(3)
        s2 = Square(4)
        with self.assertRaises(TypeError):
            Square.save_to_file([s1], [s2])

    def test_square_save_to_file_less_args(self):
        """ test save to file with less args """

        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_square_create(self):
        """ test the create method """

        obj_dict = {"id": 2, "size": 3, "y": 5, "x": 2}
        s1 = Square.create(**obj_dict)

        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 5)

        s2 = Square(5)
        s2_dict = s2.to_dictionary()
        s3 = Square.create(**s2_dict)

        self.assertFalse(s2 is s3)
        self.assertEqual(s3.id, 2)
        self.assertEqual(s3.width, 5)
        self.assertEqual(s3.height, 5)
        self.assertEqual(s3.size, 5)
        self.assertEqual(s3.x, 0)
        self.assertEqual(s3.y, 0)

    def test_square_create_no_args(self):
        """ test create method with no args """

        s1 = Square.create()
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_load_from_file(self):
        """ test the load_from_file method """

        s1 = Square(10, 2, 4)
        s2 = Square(4)
        sqr_list = [s1, s2]

        Square.save_to_file(sqr_list)
        sqr_list_output = Square.load_from_file()

        self.assertTrue(sqr_list_output[0] is not s1)
        self.assertTrue(sqr_list_output[1] is not s2)

        for i in range(2):
            self.assertEqual(sqr_list_output[i].id, sqr_list[i].id)
            self.assertEqual(sqr_list_output[i].height, sqr_list[i].height)
            self.assertEqual(sqr_list_output[i].width, sqr_list[i].width)
            self.assertEqual(sqr_list_output[i].size, sqr_list[i].size)
            self.assertEqual(sqr_list_output[i].x, sqr_list[i].x)
            self.assertEqual(sqr_list_output[i].y, sqr_list[i].y)

    def test_rect_load_from_file_args(self):
        """ test the load from file method with args """

        s1 = Square(3)
        s2 = Square(5)
        sqr_list = [s1, s2]

        Square.save_to_file(sqr_list)

        with self.assertRaises(TypeError):
            list_output = Square.load_from_file(3)

    def test_square_save_to_file_csv(self):
        """ test the save to file csv method """

        s1 = Square(6)
        s2 = Square(4, 1, 3, 1)
        Square.save_to_file_csv([s1, s2])

        sqr_file = Path("Square.csv")
        self.assertTrue(sqr_file.is_file())

        exp_str = "1,6,0,0\n1,4,1,3\n"
        with open(sqr_file, "r") as f:
            self.assertEqual(f.read(), exp_str)

    def test_square_save_to_file_csv2(self):
        """ test the save to file csv method """

        s1 = Square(5, 3, 1)
        Square.save_to_file_csv([s1])

        sqr_file = Path("Square.csv")
        self.assertTrue(sqr_file.is_file())

        with open(sqr_file, "r") as f:
            self.assertEqual(f.read(), "1,5,3,1\n")

    def test_square_save_to_file_csv3(self):
        """ test the save to file csv method """

        s1 = Square(2)
        s2 = Square(2, 4, 1, 1)
        s3 = Square(4, 1, 2)
        Square.save_to_file_csv([s1, s2, s3])

        sqr_file = Path("Square.csv")
        self.assertTrue(sqr_file.is_file())

        exp_str = "1,2,0,0\n1,2,4,1\n2,4,1,2\n"
        with open(sqr_file, "r") as f:
            self.assertEqual(f.read(), exp_str)

    def test_square_save_to_file_csv_none(self):
        """ test the save to file csv method with none """

        Square.save_to_file_csv(None)

        sqr_file = Path("Square.csv")
        self.assertTrue(sqr_file.is_file())

        with open(sqr_file, "r") as f:
            self.assertEqual(f.read(), "[]\n")

    def test_square_save_to_file_more_args(self):
        """  test save to file csv with more args than expected """

        s1 = Square(3)
        s2 = Square(4)
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([s1], [s2])

    def test_square_load_from_file_csv(self):
        """ test the load_from_file_csv method """

        s1 = Square(10, 2, 4)
        s2 = Square(4)
        sqr_list = [s1, s2]

        Square.save_to_file_csv(sqr_list)
        sqr_list_output = Square.load_from_file_csv()

        self.assertTrue(sqr_list_output[0] is not s1)
        self.assertTrue(sqr_list_output[1] is not s2)

        for i in range(2):
            self.assertEqual(sqr_list_output[i].id, sqr_list[i].id)
            self.assertEqual(sqr_list_output[i].height, sqr_list[i].height)
            self.assertEqual(sqr_list_output[i].width, sqr_list[i].width)
            self.assertEqual(sqr_list_output[i].size, sqr_list[i].size)
            self.assertEqual(sqr_list_output[i].x, sqr_list[i].x)
            self.assertEqual(sqr_list_output[i].y, sqr_list[i].y)

    def test_rect_load_from_file_csv_args(self):
        """ test the load from file csv method with args """

        s1 = Square(3)
        s2 = Square(5)
        sqr_list = [s1, s2]

        Square.save_to_file_csv(sqr_list)

        with self.assertRaises(TypeError):
            list_output = Square.load_from_file_csv(3)
