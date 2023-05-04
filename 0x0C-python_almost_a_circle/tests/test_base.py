#!/usr/bin/python3
""" Testing the base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Testing the base class file """

    def test_base(self):
        """ testing the initialization """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b10 = Base()
        self.assertTrue(type(b1) == type(b10))
        self.assertFalse(b1.id == b10.id)


if __name__ == '__main__':
    unittest.main()

