""""
Module will run unittests for fibonacci.py
Yvonne Cheng 
csci 112
Winter, 2023
"""
import unittest
from matrix import Matrix
from fibonacci import *

class TestFibonacci(unittest.TestCase):

    def test_powexp(self):
        self.assertEqual(powexponential(0), 0)
        self.assertEqual(powexponential(1), 1)
        self.assertEqual(powexponential(2), 1)
        self.assertEqual(powexponential(5), 5)
        self.assertEqual(powexponential(10), 55)

    def test_powlinear(self):
        self.assertEqual(powlinear(0), 0)
        self.assertEqual(powlinear(1), 1)
        self.assertEqual(powlinear(2), 1)
        self.assertEqual(powlinear(5), 5)
        self.assertEqual(powlinear(10), 55)

    def test_powlog(self):
        self.assertEqual(powlog(0), 0)
        self.assertEqual(powlog(1), 1)
        self.assertEqual(powlog(2), 1)
        self.assertEqual(powlog(5), 5)
        self.assertEqual(powlog(10), 55)
      

if __name__ == '__main__':
    unittest.main()

