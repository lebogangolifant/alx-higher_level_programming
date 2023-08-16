#!/usr/bin/python3
"""Unittests a for Base Class"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id(self):
        # Test that the id attribute is assigned correctly
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    def test_to_json_string(self):
        # Test the to_json_string method
        b1 = Base()
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_from_json_string(self):
        # Test the from_json_string method
        json_string = '[{"id": 1}, {"id": 2}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"id": 1}, {"id": 2}])

    def test_create(self):
        # Test the create method
        b1 = Base(1)
        dictionary = b1.to_dictionary()
        b2 = Base.create(**dictionary)
        self.assertEqual(b1, b2)
        self.assertFalse(b1 is b2)

if __name__ == '__main__':
    unittest.main()
