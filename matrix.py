""""
Module of class Maxtrix to solve problems in lab02 
Yvonne Cheng 
csci 112
Winter, 2023
"""

#Create Matrix class using iterable length of rows * columns 
class Matrix:
    def __init__(self, row, column, iterable):
        self.row = row
        self.column = column
        self.iterable = iterable
        self.matrix = [[iterable[i] for i in range(j*column, column*j + column)] for j in range(row)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    
    #Peforms matrix multiplication
    #If second element is float or int, multiply each element in the matrix by that value. 
    #If second element is another Matrix object, perform matrix multiplication. 
    #Else, if the # of columns of first matrix != the # of rows in the second matrix, raise ValueError
    def __mul__(self, other):
        while True:
            if isinstance(other, float) or isinstance(other, int):
                return Matrix(self.row, self.column, [other * element for row in self.matrix for element in row])
                break
            if isinstance(other, Matrix) and other.row == self.column:
                return Matrix(self.row, other.column, [sum(self.matrix[i][j] * other.matrix[j][k] 
                for j in range(self.column)) for i in range(self.row) for k in range(other.column)])
                break
            raise ValueError("Invalid")

    #If matrix is not square, rasie ValueError
    #If power == 0, return an identity matrix using Matrix class
    #If power == 1, return matrix
    #If power % 2, return matrix times itself that number of times
    # If power % 2 == 1, meaning power odd, return matrix times itself to the power-1 times
    def __pow__(self, pow):
        if self.row != self.column:
            raise ValueError("Matrix not square")
        if pow == 0:
            return Matrix(self.row, self.column, [1 if i == j else 0 for i in range(self.column) for j in range(self.row)])
        if pow == 1:
            return self
        if pow % 2 == 0:
            return (self * self) ** (pow // 2)
        if pow % 2 == 1:
            return self * (self * self) ** (pow // 2)


if __name__ == "__main__":
    print("="*60)
    print("Problem 1:")
    m1 = Matrix (3,4, range (3*4))
    print(m1)
    print("-"*40)
    print(m1 * Matrix (4,3, range (4*3)))
    print("-"*40)
    m2 = Matrix (2, 2, [0 ,1 ,1 ,1])
    print(m2)
    print("-"*40)
    print(m2 * m2)
    print("-"*40)
    print(m2 ** 2)
    print("-"*40)
    m3 = Matrix (2,2, "abcd ")
    print(m3)

