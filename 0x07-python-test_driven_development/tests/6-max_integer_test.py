#!/usr/bin/python3
"""Max integer - Unittest """


import sys
import unittest


sys.path.append('..')
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ constructor """
    def test_ten_scale(self):
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)
        self.assertEqual(max_integer([40, 20, 30, 10]), 40)
        self.assertEqual(max_integer([10, 20, 77, 40, 7]), 77)

    def test_negative_charge(self):
        l = [-23, -48, -13, -7]
        self.assertEqual(max_integer(l), -7)

    def test_alone(self):
        l = [7]
        self.assertEqual(max_integer(l), 7)

    def test_none(self):
        l = []
        self.assertEqual(max_integer(l), None)

    def test_float_charge(self):
        l = [1.0, 2.0, 3.0, 7.0]
        self.assertEqual(max_integer(l), 7.0)

    def test_two_max_numbers(self):
        l = [1, 2, 3, 7, 5, 7]
        self.assertEqual(max_integer(l), 7)

    def test_string(self):
        l = "testify"
        self.assertEqual(max_integer(l), 'y')

    def test_mix_list(self):
        l = ['T', 7, 3.0]
        with self.assertRaises(TypeError):
            max_integer(l)

if __name__ == '__main__':
    unittest.main()
