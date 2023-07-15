#!/usr/bin/python3
"""Unittest module for a square class"""


import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(5)
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        # Redirect stdout to capture the print output
        with captured_output() as (out, _):
            s.display()
        output = out.getvalue()
        self.assertEqual(output, expected_output)

    def test_str(self):
        s = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(s), expected_output)

    def test_update(self):
        s = Square(5, 2, 3, 1)
        s.update(10, 7, 4, 5)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertDictEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
