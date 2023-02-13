import unittest
import io
import sys
import json
from pathlib import Path
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """ Test the rectangle class """

    def setUp(self):
        """ set up """

        Base._Base__nb_objects = 0

    def test_rect(self):
        """ test normal rect"""

        r1 = Rectangle(10, 5, 7, 2, 5)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 5)

    def test_rect2(self):
        """ test normal rect """

        r1 = Rectangle(1, 1)

        r1.id = 5
        self.assertEqual(r1.id, 5)
        r1.height = 10
        self.assertEqual(r1.height, 10)
        r1.width = 3
        self.assertEqual(r1.width, 3)
        r1.x = 4
        self.assertEqual(r1.x, 4)
        r1.y = 2
        self.assertEqual(r1.y, 2)

    def test_rect_no_id(self):
        """ test rect without id """

        r1 = Rectangle(5, 17, 9, 15)

        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 15)
        self.assertEqual(r1.id, 1)

    def test_rect_no_y(self):
        """ test rect without y """

        r1 = Rectangle(200, 10, 17)

        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 17)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_rect_invalid_y1(self):
        """ test rect with wrong y """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(200, 10, 17, "s")
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 5, 20, True)
        with self.assertRaises(TypeError):
            r3 = Rectangle(15, 20, 25, {"y": 1})
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 1, 1, [1, 2])
        with self.assertRaises(TypeError):
            r5.y = "hello"
        with self.assertRaises(TypeError):
            r5.y = {"y": 1}
        with self.assertRaises(TypeError):
            r5.y = (2, 3)
        with self.assertRaises(TypeError):
            r5.y = True

    def test_rect_invalid_y2(self):
        """ test rect with wrong y """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(200, 10, 17, -5)
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 5, 20, -10)
        with self.assertRaises(ValueError):
            r5.y = -2
        with self.assertRaises(ValueError):
            r5.y = -100000

    def test_rect_no_x(self):
        """ test rect without x """

        r1 = Rectangle(20, 117)

        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 117)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_rect_invalid_x1(self):
        """ test rect with wrong x """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(200, 10, "hello", 17)
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 5, False, 12)
        with self.assertRaises(TypeError):
            r3 = Rectangle(15, 20, {"y": 1})
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 1, [1], 20)
        with self.assertRaises(TypeError):
            r5.x = "s"
        with self.assertRaises(TypeError):
            r5.x = {"x": 1}
        with self.assertRaises(TypeError):
            r5.x = (1, 1)
        with self.assertRaises(TypeError):
            r5.x = True

    def test_rect_invalid_x2(self):
        """ test rect with wrong x """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(200, 10, -5, 10)
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 5, -10)
        with self.assertRaises(ValueError):
            r5.x = -5
        with self.assertRaises(ValueError):
            r5.x = -256

    def test_rect_no_height(self):
        """ test rect without height """

        with self.assertRaises(TypeError):
            r1 = Rectangle(20)

    def test_rect_invalid_height1(self):
        """ test rect with wrong height """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(200, "s", 10, 20)
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, False, 0)
        with self.assertRaises(TypeError):
            r3 = Rectangle(15, {"y": 1}, 25)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, [1, 2], 0, 0)
        with self.assertRaises(TypeError):
            r5.height = "hello"
        with self.assertRaises(TypeError):
            r5.height = {"y": 1}
        with self.assertRaises(TypeError):
            r5.height = (17, 5)
        with self.assertRaises(TypeError):
            r5.height = True

    def test_rect_invalid_height2(self):
        """ test rect with wrong height """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(200, -5, 20)
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, -10)
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            r5.height = -2
        with self.assertRaises(ValueError):
            r5.height = 0
        with self.assertRaises(ValueError):
            r5.height = -500

    def test_rect_no_width(self):
        """ test rect without width """

        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_rect_invalid_width1(self):
        """ test rect with wrong width """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 10, 20)
        with self.assertRaises(TypeError):
            r2 = Rectangle(False, 20)
        with self.assertRaises(TypeError):
            r3 = Rectangle({"y": 1}, 25)
        with self.assertRaises(TypeError):
            r4 = Rectangle([1, 2], 1, 0)
        with self.assertRaises(TypeError):
            r5.width = "hello"
        with self.assertRaises(TypeError):
            r5.width = {"y": 1}
        with self.assertRaises(TypeError):
            r5.width = [1]
        with self.assertRaises(TypeError):
            r5.width = True

    def test_rect_invalid_width2(self):
        """ test rect with wrong width """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(-5, 20)
        with self.assertRaises(ValueError):
            r2 = Rectangle(-10, 15)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r5.width = -2
        with self.assertRaises(ValueError):
            r5.width = 0
        with self.assertRaises(ValueError):
            r5.width = -500

    def test_rect_more_args(self):
        """ test rect with more args than expected """

        with self.assertRaises(TypeError):
            r1 = Rectangle(12, 2, 0, 0, 1, 17)

    def test_rect_area(self):
        """ test rect area """

        r1 = Rectangle(1, 15)
        self.assertEqual(r1.area(), 15)

        r2 = Rectangle(3, 15)
        self.assertEqual(r2.area(), 45)

        r3 = Rectangle(2, 5)
        self.assertEqual(r3.area(), 10)

        r4 = Rectangle(12, 10)
        self.assertEqual(r4.area(), 120)

        r4.width = 5
        self.assertEqual(r4.area(), 50)

        r4.height = 12
        self.assertEqual(r4.area(), 60)

    def test_rect_area_args(self):
        """ test rect area with args """

        r1 = Rectangle(12, 10)

        with self.assertRaises(TypeError):
            r1.area(12)

    def test_rect_str(self):
        """ test the __str__ method """

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(10, 5)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 0/0 - 10/5")

        r3 = Rectangle(1, 17, 2)
        self.assertEqual(r3.__str__(), "[Rectangle] (2) 2/0 - 1/17")

    def test_rect_str_args(self):
        """ test __str__ method with args """
        r1 = Rectangle(1, 13)

        with self.assertRaises(TypeError):
            r1.__str__("hey")

    def test_rect_display(self):
        """ test the display method """

        r1 = Rectangle(3, 4)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "###\n###\n###\n###\n")

    def test_rect_display2(self):
        """ test the display method """

        r1 = Rectangle(5, 5, 3, 2)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__

        exp_output = "\n\n   #####\n   #####\n   #####\n   #####\n   #####\n"
        self.assertEqual(output.getvalue(), exp_output)

    def test_rect_display3(self):
        """ test the display method """

        r1 = Rectangle(2, 1, 1, 0)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), " ##\n")

    def test_rect_display4(self):
        """ test the display method """

        r1 = Rectangle(4, 3, 0, 5)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "\n\n\n\n\n####\n####\n####\n")

    def test_rect_display_args(self):
        """ test display with args """

        r1 = Rectangle(2, 4)

        with self.assertRaises(TypeError):
            r1.display([])

    def test_rect_update_args(self):
        """ test rect update with args"""

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(2)
        self.assertEqual(r1.id, 2)

        r1.update(10, 5, 3)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(1, 17, 4, 5, 7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 17)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)

        # update with extra values in args
        r1.update(15, 2, 34, 33, 22, 12, 22)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 34)
        self.assertEqual(r1.x, 33)
        self.assertEqual(r1.y, 22)

        # if args and kwargs is given, args is used
        r1.update(1, 20, 11, 8, 2, height=1, id=5, x=2, y=4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 2)

    def test_rect_update_invalid_args1(self):
        """ test update with invalid args """

        r1 = Rectangle(16, 12)

        # width errors
        with self.assertRaises(TypeError):
            r1.update(1, "s", 10)
        with self.assertRaises(TypeError):
            r1.update(2, True, 15)
        with self.assertRaises(TypeError):
            r1.update(1, [1], 30)
        with self.assertRaises(TypeError):
            r1.update(2, {"y": 15}, 25)

        # height errors
        with self.assertRaises(TypeError):
            r1.update(13, 20, "hello")
        with self.assertRaises(TypeError):
            r1.update(1, 12, False)
        with self.assertRaises(TypeError):
            r1.update(1, 15, [1])
        with self.assertRaises(TypeError):
            r1.update(1, {"y": 15}, 25)

        # x errors
        with self.assertRaises(TypeError):
            r1.update(12, 20, 15, "13")
        with self.assertRaises(TypeError):
            r1.update(1, 5, 2, False)
        with self.assertRaises(TypeError):
            r1.update(2, 15, 17, [1])
        with self.assertRaises(TypeError):
            r1.update(3, 20, 20, {"y": 15}, 25)

        # y errors
        with self.assertRaises(TypeError):
            r1.update(1, 20, 15, 0, "13")
        with self.assertRaises(TypeError):
            r1.update(2, 5, 2, 12, True)
        with self.assertRaises(TypeError):
            r1.update(3, 15, 17, 1, [1, 2])
        with self.assertRaises(TypeError):
            r1.update(4, 25, 20, 20, {"y": 15}, 25)

    def test_rect_update_invalid_args2(self):
        """ test update with invalid args """

        r1 = Rectangle(16, 12)

        # width errors
        with self.assertRaises(ValueError):
            r1.update(1, -5, 10)
        with self.assertRaises(ValueError):
            r1.update(1, 0, 15)

        # height errors
        with self.assertRaises(ValueError):
            r1.update(1, 13, -2)
        with self.assertRaises(ValueError):
            r1.update(2, 1, 0)

        # x errors
        with self.assertRaises(ValueError):
            r1.update(12, 20, 15, -17)

        # y errors
        with self.assertRaises(ValueError):
            r1.update(2, 15, 2, 0, -20)

    def test_rect_update_kwargs(self):
        """ test update with kwargs """

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(id=10, width=5)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)

        r1.update(height=2, x=17)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 17)
        self.assertEqual(r1.y, 10)

        r1.update(height=13, y=5, x=17, id=2, width=7)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 17)
        self.assertEqual(r1.y, 5)

    def test_rect_update_invalid_kwargs1(self):
        """ test update with invalid kwargs """

        r1 = Rectangle(16, 12)
        invalid_t = ["s", (1, 2), True, False, "65", [1], {"w": 5}]

        # width errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                r1.update(width=typ, id=1)

        # height errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                r1.update(height=typ)

        # x errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                r1.update(x=typ, width=2, height=15)

        # y errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                r1.update(x=0, y=typ)

    def test_update_invalid_kwargs2(self):
        """ test update with invalid kwargs """

        r1 = Rectangle(16, 12)

        # width errors
        with self.assertRaises(ValueError):
            r1.update(width=-5)
        with self.assertRaises(ValueError):
            r1.update(width=0, id=3)

        # height errors
        with self.assertRaises(ValueError):
            r1.update(height=-2)
        with self.assertRaises(ValueError):
            r1.update(x=0, width=20, height=0)

        # x errors
        with self.assertRaises(ValueError):
            r1.update(id=5, x=-17)

        # y errors
        with self.assertRaises(ValueError):
            r1.update(y=-20)

    def test_rect_update_less_args(self):
        """ test update method with less args """

        r1 = Rectangle(12, 3)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        # when update is called with no args, rect does not change
        r1.update()

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rect_to_dictionary(self):
        """ test the to_dictionary method """

        r1 = Rectangle(10, 2, 1, 2, 5)
        dict_r1 = r1.to_dictionary()
        self.assertEqual(dict_r1["id"], 5)
        self.assertEqual(dict_r1["x"], 1)
        self.assertEqual(dict_r1["y"], 2)
        self.assertEqual(dict_r1["width"], 10)
        self.assertEqual(dict_r1["height"], 2)

        r1.update(1, 5, 13)
        dict_r1 = r1.to_dictionary()
        self.assertEqual(dict_r1["id"], 1)
        self.assertEqual(dict_r1["x"], 1)
        self.assertEqual(dict_r1["y"], 2)
        self.assertEqual(dict_r1["width"], 5)
        self.assertEqual(dict_r1["height"], 13)

    def test_rect_to_dictionary_err(self):
        """ test to_dictionary with error """

        r1 = Rectangle(12, 5)
        dict_r1 = r1.to_dictionary()

        with self.assertRaises(KeyError):
            dict_r1["size"]

    def test_rect_to_dictionary_args(self):
        """ test to_dictionary method with args """

        r1 = Rectangle(10, 4)

        with self.assertRaises(TypeError):
            dict_r1 = r1.to_dictionary(1)

    def test_rect_save_to_file(self):
        """ test the save to file method """

        r1 = Rectangle(5, 6)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])

        rect_file = Path("Rectangle.json")
        self.assertTrue(rect_file.is_file())

        rect_list = [r1.to_dictionary(), r2.to_dictionary()]
        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), json.dumps(rect_list))

    def test_rect_save_to_file2(self):
        """ test the save to file method """

        r1 = Rectangle(2, 5, 3)
        Rectangle.save_to_file([r1])

        rect_file = Path("Rectangle.json")
        self.assertTrue(rect_file.is_file())

        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), json.dumps([r1.to_dictionary()]))

    def test_rect_save_to_file3(self):
        """ test the save to file method """

        r1 = Rectangle(2, 5, 3)
        r2 = Rectangle(2, 4, 1, 1)
        r3 = Rectangle(4, 5)
        Rectangle.save_to_file([r1, r2, r3])

        rect_file = Path("Rectangle.json")
        self.assertTrue(rect_file.is_file())

        rect_list = [
            r1.to_dictionary(),
            r2.to_dictionary(),
            r3.to_dictionary()
        ]
        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), json.dumps(rect_list))

    def test_rect_save_to_file_none(self):
        """ test the save to file method with none """

        Rectangle.save_to_file(None)

        rect_file = Path("Rectangle.json")
        self.assertTrue(rect_file.is_file())

        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rect_save_to_file_more_args(self):
        """  test save to file with more args than expected """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 3)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([r1], [r2])

    def test_rect_save_to_file_less_args(self):
        """ test save to file with less args """

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_rect_create(self):
        """ test the create method """

        obj_dict = {"id": 2, "width": 3, "height": 5, "x": 2}
        r1 = Rectangle.create(**obj_dict)

        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 2)
        r2_dict = r2.to_dictionary()
        r3 = Rectangle.create(**r2_dict)

        self.assertFalse(r2 is r3)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_rect_create_no_args(self):
        """ test create method with no args """

        r1 = Rectangle.create()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rect_load_from_file(self):
        """ test the load_from_file method """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        rect_list = [r1, r2]

        Rectangle.save_to_file(rect_list)
        rect_list_output = Rectangle.load_from_file()

        self.assertTrue(rect_list_output[0] is not r1)
        self.assertTrue(rect_list_output[1] is not r2)

        for i in range(2):
            self.assertEqual(rect_list_output[i].id, rect_list[i].id)
            self.assertEqual(rect_list_output[i].height, rect_list[i].height)
            self.assertEqual(rect_list_output[i].width, rect_list[i].width)
            self.assertEqual(rect_list_output[i].x, rect_list[i].x)
            self.assertEqual(rect_list_output[i].y, rect_list[i].y)

    def test_rect_load_from_file_args(self):
        """ test the load from file method with args """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(5, 2)
        rect_list = [r1, r2]

        Rectangle.save_to_file(rect_list)

        with self.assertRaises(TypeError):
            list_output = Rectangle.load_from_file(3)

    def test_rect_save_to_file_csv(self):
        """ test the save to file csv method """

        r1 = Rectangle(5, 6)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file_csv([r1, r2])

        rect_file = Path("Rectangle.csv")
        self.assertTrue(rect_file.is_file())

        exp_str = "1,5,6,0,0\n2,2,4,1,1\n"
        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), exp_str)

    def test_rect_save_to_file_csv2(self):
        """ test the save to file csv method """

        r1 = Rectangle(2, 5, 3)
        Rectangle.save_to_file_csv([r1])

        rect_file = Path("Rectangle.csv")
        self.assertTrue(rect_file.is_file())

        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), "1,2,5,3,0\n")

    def test_rect_save_to_file_csv3(self):
        """ test the save to file csv method """

        r1 = Rectangle(2, 5, 3)
        r2 = Rectangle(2, 4, 1, 1)
        r3 = Rectangle(4, 5)
        Rectangle.save_to_file_csv([r1, r2, r3])

        rect_file = Path("Rectangle.csv")
        self.assertTrue(rect_file.is_file())

        exp_str = "1,2,5,3,0\n2,2,4,1,1\n3,4,5,0,0\n"
        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), exp_str)

    def test_rect_save_to_file_csv_none(self):
        """ test the save to file csv method with none """

        Rectangle.save_to_file_csv(None)

        rect_file = Path("Rectangle.csv")
        self.assertTrue(rect_file.is_file())

        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), "[]\n")

    def test_rect_save_to_file_csv_more_args(self):
        """  test save to file csv with more args than expected """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 3)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([r1], [r2])

    def test_rect_save_to_file_less_args(self):
        """ test save to file with less args """

        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_rect_load_from_file_csv(self):
        """ test the load_from_file_csv method """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        rect_list = [r1, r2]

        Rectangle.save_to_file_csv(rect_list)
        rect_list_output = Rectangle.load_from_file_csv()

        self.assertTrue(rect_list_output[0] is not r1)
        self.assertTrue(rect_list_output[1] is not r2)

        for i in range(2):
            self.assertEqual(rect_list_output[i].id, rect_list[i].id)
            self.assertEqual(rect_list_output[i].height, rect_list[i].height)
            self.assertEqual(rect_list_output[i].width, rect_list[i].width)
            self.assertEqual(rect_list_output[i].x, rect_list[i].x)
            self.assertEqual(rect_list_output[i].y, rect_list[i].y)

    def test_rect_load_from_file_csv_args(self):
        """ test the load from file csv method with args """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(5, 2)
        rect_list = [r1, r2]

        Rectangle.save_to_file_csv(rect_list)

        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv(rect_list)
