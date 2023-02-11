import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ class to test the Base class """

    def test_base(self):
        """ test the base class """

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(1)
        self.assertEqual(b2.id, 1)

        b3 = Base()
        self.assertEqual(b3.id, 2)

        b4 = Base(200)
        self.assertEqual(b4.id, 200)

        b5 = Base(None)
        self.assertEqual(b5.id, 3)

        b6 = Base(-10)
        self.assertEqual(b6.id, -10)

        b7 = Base(0)
        self.assertEqual(b7.id, 0)
