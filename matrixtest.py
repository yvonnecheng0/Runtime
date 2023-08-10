""""
Module will run unittests for matrix.py 
Yvonne Cheng 
csci 112
Winter, 2023
"""

import unittest
from matrix import Matrix

class MatrixTest(unittest.TestCase):
    def test_init(self):
        matrix = Matrix(2, 2, [1, 2, 3, 4])
        self.assertEqual(matrix.row, 2)
        self.assertEqual(matrix.column, 2)
        self.assertEqual(matrix.matrix, [[1, 2], [3, 4]])

    def test_str(self):
        matrix = Matrix(2, 2, [1, 2, 3, 4])
        self.assertEqual(str(matrix), "1 2\n3 4")

    def test_mul1(self):
        matrix = Matrix(2, 2, [1, 2, 3, 4])
        result = matrix * 2
        self.assertEqual(result.matrix, [[2, 4], [6, 8]])

    def test_mul2(self):
        matrix_1 = Matrix(2, 2, [1, 2, 3, 4])
        matrix_2 = Matrix(2, 2, [7, 6, 2, 9])
        result = matrix_1 * matrix_2
        self.assertEqual(result.matrix, [[11, 24], [29, 54]])

    def test_zeropow(self):
        matrix = Matrix(2, 2, [1, 2, 3, 4])
        result = matrix ** 0
        self.assertEqual(result.matrix, [[1, 0], [0, 1]])

    def test_onepow(self):
        matrix = Matrix(2, 2, [2, 3, 4, 5])
        result = matrix ** 1
        self.assertEqual(result.matrix, [[2, 3], [4, 5]])

    def test_evenpow(self):
        matrix = Matrix(2, 2, [2, 3, 4, 5])
        result = matrix ** 2
        self.assertEqual(result.matrix, [[16, 21], [28, 37]])

    def test_oddpow(self):
        matrix = Matrix(2, 2, [2, 3, 4, 5])
        result = matrix ** 3
        self.assertEqual(result.matrix, [[116, 153], [204, 269]])

if __name__ == '__main__':
    unittest.main()


