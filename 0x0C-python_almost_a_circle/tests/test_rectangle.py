#!/usr/bin/python3
""" unittest for rectangle class """

import unittest
from models.rectangle import Rectangle as rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """ test for rectangle class """
    def test_init(self):
        with self.assertRaises(ValueError):
            r1 = rectangle(-3, -5)
        self.assertTrue(issubclass(rectangle, Base))
        with self.assertRaises(TypeError):
            r1 = rectangle(3, 'k')
            r1 = rectangle('k', 3)
        with self.assertRaises(ValueError):
            r1 = rectangle(3, 5, -1)
            r1 = rectangel(3, 5, y=-1)
        r1 = rectangle(3, 4)
        r2 = rectangle(3, 4)
        self.assertFalse(r1.id == r2.id) 

    def test_area(self):
        r1 = rectangle(3, 5)
        self.assertTrue(r1.area() == 15)


    def test_print(self):
        """ function to test the print function """
        r1 = rectangle(2, 2)
        self.assertTrue(4 == r1.display())
        
    def test_str(self):
        r1 = rectangle(4, 6, 2, 1, 12)
        self.assertTrue(r1.__str__() == '[Rectangle] (12) 2/1 - 4/6')

    def test_updateArgs(self):
        """ testing the update method of the rectangle class """ 
        r1 = rectangle(10, 10, 10, 10)
        r1.update(89,2,3,4,5)
        self.assertTrue(r1.__str__() == '[Rectangle] (89) 4/5 - 2/3')

    def test_updateKwargs(self):
        r1 = rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertTrue(r1.__str__() == '[Rectangle] (89) 1/3 - 4/2')

if __name__ == '__main__':
    unittest.main()
