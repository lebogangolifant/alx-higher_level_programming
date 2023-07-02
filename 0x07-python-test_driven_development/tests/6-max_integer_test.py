#!/usr/bin/python3
"""
Unittests for the max_integer function.
"""

import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_empty_list(self):
        """
        Test the max_integer function with an empty list.
        The function should return None.
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """
        Test the max_integer function with a list containing a single element.
        The function should return the same element.
        """
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """
        Test the max_integer function with a list of positive numbers.
        The function should return the maximum value.
        """
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """
        Test the max_integer function with a list of negative numbers.
        The function should return the maximum value.
        """
        result = max_integer([-2, -4, -1, -5, -3])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """
        Test the function with a list of mixed positive and negative numbers.
        The function should return the maximum value.
        """
        result = max_integer([-2, 4, -1, 5, -3])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        """
        Test the max_integer function with a list containing duplicate numbers.
        The function should return the maximum value.
        """
        result = max_integer([3, 5, 2, 4, 5])
        self.assertEqual(result, 5)

    def test_large_numbers(self):
        """
        Test the max_integer function with a list of large numbers.
        The function should return the maximum value.
        """
        result = max_integer([1000000, 2000000, 3000000, 1500000])
        self.assertEqual(result, 3000000)


if __name__ == '__main__':
    unittest.main()
