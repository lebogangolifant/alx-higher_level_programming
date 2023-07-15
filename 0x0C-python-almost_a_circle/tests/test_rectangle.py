#!/usr/bin/python3
"""Unittest for Rectangle Class"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(5, 5)
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        # Redirect stdout to capture the print output
        with captured_output() as (out, _):
            r.display()
        output = out.getvalue()
        self.assertEqual(output, expected_output)

    def test_str(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(10, 7, 8, 4, 5)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        }
        self.assertDictEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
