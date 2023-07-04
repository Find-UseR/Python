# Code for finding basis from set of vectors for nonSquare Matrix
import numpy as np

a = eval(input("Input size of the space"))
b = eval(input("Input Number of Vectors"))
c = 1
matrix = []
vector = []
for i in range(b):
    r = 1
    column = []
    for i in range(a):
        print("Enter value of column", c)
        x = eval(input())
        column.append(x)
        r = r + 1
    c = c + 1
    matrix.append(column)
matrix = np.asarray(matrix)
matrix = np.transpose(matrix)
print("Our Required Matrix=", matrix)
aug = np.copy(matrix)


def row_interchange(mat, row1, row2):
    t1 = mat[row1].copy()
    t2 = mat[row2].copy()
    mat[row1] = t2
    mat[row2] = t1
    return mat
    ####################


def scalar_multiply(mat, scalar):
    return mat * scalar
    ###############################


def row_addition(mat, vect, rownum):
    mat[rownum] = mat[rownum] + vect
    return mat


for i in range(0, b):
    for j in range(i + 1, a):
        ratio = aug[j][i] / aug[i][i]
        mul_result = scalar_multiply(aug[i], ratio)  # row1*ratio
        print("Multiplied Result", mul_result)
        aug = row_addition(aug, -mul_result, j)
        print("My new Augmented Matrix=", aug)
for i in range(a):
    for j in range(b):
        if aug[i][j] != 0:
            print("Your Vector", matrix[:, j])
            break
