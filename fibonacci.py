""""
Module will execute in exponential time, O(2n), one in linear time, O(n), and one in log time O(log n) 
based on calculating the powers of the matrix [0 1 1 1]
Yvonne Cheng 
csci 112
Winter, 2023
"""
from matrix import Matrix

# Exponential time algorithm
def powexponential(n):
    if n in [0, 1]:
        return n
    else:
        return powexponential(n-1) + powexponential(n-2)

# Linear time algorithm
def powlinear(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return c

# Log time algorithm using Matrix class based on calculating the powers of the matrix
def powlog(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        matrix = Matrix(2, 2, [1, 1, 1, 0])
        result_matrix = matrix ** (n-1)
        return result_matrix.matrix[0][0]

if __name__ == "__main__":
    print(powexponential(10))
    print(powlinear(10))
    print(powlog(10))




