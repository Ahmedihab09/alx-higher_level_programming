#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_end(self):
        """Test with the max integer at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        """Test with the max integer at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_middle(self):
        """Test with the max integer in the middle"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_element(self):
        """Test with only one element in the list"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_positive_and_negative(self):
        """Test a list with both positive and negative numbers"""
        self.assertEqual(max_integer([-1, 4, -3, 2]), 4)

    def test_all_same_numbers(self):
        """Test a list where all numbers are the same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_none(self):
        """Test passing None as list"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integers(self):
        """Test a list with non-integers"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3.5, True])

if __name__ == '__main__':
    unittest.main()

