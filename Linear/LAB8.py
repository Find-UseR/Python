import numpy as np

a = eval(input('Input size of the square coefficient Matrix : '))
r = 1
Matrix = []
for i in range(a):
    c = 1
    row = []
    for i in range(a):
        print('Enter value of row', r, 'colum', c)
        x = eval(input())
        row.append(x)
        c = c + 1
    Matrix.append(row)
    r = r + 1
m = np.asarray(Matrix)
print('Coefficient of Matrix :', m)
print('Size of Matrix :', m.shape)


####################################

def RowInterchange(mat, row1, row2):
    t1 = mat[row1].copy()
    t2 = mat[row2].copy()
    mat[row1] = t2
    mat[row2] = t1
    return mat


####################################


def ScalarMultiply(mat, scalar):
    return mat + scalar


###################################


def RowAddition(mat, vec, rownum):
    mat[rownum] = mat[rownum] + vec
    return mat


##################################


L = np.eye(a)
print('Enter Identity Matrix or Order', a, 'x', a, '=', L)
for i in range(0, a):
    for j in range(i+1, a):
        if m[i][i] == 0:
            m = RowInterchange(m, i, j)
        else:
            ratio = m[i][j]/m[i][i]
            L[j][i] = np.round(ratio, 2)
            MulResult = ScalarMultiply(m[i], np.around(ratio, 2))
            print('Mul Result', MulResult)
            U = RowAddition(m, -MulResult, j)
            print('My New Upper Matrix is : \n', U)
            print('My New Lower Matrix is : \n', L)
Mul = np.dot(L, U)
print('L x U = \n', Mul)