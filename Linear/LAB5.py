# Construction of function for row interchange
import numpy as np

Mat1 = np.array([[2, 3, -4], [4, 6, 1, ], [3, 7, -2]])
print("your original matrix is=", Mat1)


def row_int(mat, r1, r2):
    t1 = mat[[r1 - 1]].copy()
    t2 = mat[[r2 - 1]].copy()
    mat[[r2 - 1]] = t2
    mat[[r1 - 1]] = t1


row_int(Mat1, 1, 2)
print(Mat1)


#Construction of function for scalar multiplication


Mat1 = np.array([[2, 3, -4], [4, 6, 1, ], [3, 7, -2]])
print("your original matrix is=", Mat1)


def sclr_mul(mat, scalar, row):
    mat[row] = scalar * mat[row]


sclr_mul(Mat1, -8, 1)  # Multiplying row 1 of matix by -8
print("after scalar multiplication Matrix is=", Mat1)
# construction of function of adding two rows
Mat1 = np.array([[2, 3, -4], [4, 6, 1, ], [3, 7, -2]])
print("your original matrix is=", Mat1)


def add_mat(Mat, r1, r2):
    Mat[r1 - 1] = Mat[r1 - 1] + Mat[r2 - 1]


add_mat(Mat1, 2, 3)
print("after addition Matrix is=", Mat1)
a = eval(input("Enter the number= "))
print("Number is: ", a)
i = 1
while i <= a:
    print(i, 'My Name is AQib')
    i = i + 1
import numpy as np

m1 = np.array([[2, 5], [3, 6]])
print("Array is: ", m1)
m2 = np.transpose(m1)
print("Transpose is: ", m2)
m3 = np.linalg.det(m1)
print("Determinant is: ", m3)
m4 = np.linalg.inv(m1)
print("Inverse is: ", m4)
m5 = np.dot(m1, m2)
print("Dot Product is: ", m5)
# Code for solving n*n system of linear equation by using inverse method
n = eval(input("Enter the size of matrix= "))
r = 1
matrix = []
while r <= n:
    c = 1
    row = []
    while c <= n:
        print("Enter the value of Row", r, "Column", c)
        x = eval(input())
        row.append(x)
        c = c + 1
    matrix.append(row)
    r = r + 1
m = np.asarray(matrix)
print("Coeffecient matrix= ", m)
m6 = np.linalg.det(m)
print("Determinant of Matrix is: ", m6)
m7 = np.linalg.inv(m)
print("Inverse of Matrix is: ", m7)
vtr1 = []
c = 1
while c <= n:
    print("Please enter the constant of equations: ")
    x = eval(input())
    vtr1.append(x)
    c = c + 1
vtr2 = np.asarray(vtr1)
ans = np.dot(m7, vtr2)
print("Answer is: ", ans)
for i in range(len(ans)):
    print("value of x[", i + 1, "]=", np.round(ans[i], 2))
det = []
ans1 = []
print("Your original matrix=", m)
print("Your original vextor=", vtr2)
for i in range(n):
    m1 = m.copy()
    m1[:, i] = vtr2
    print("after=", m1)
    d = np.linalg.det(m1)
    ans1.append(d / n5)
ans1 = np.asarray(ans1)
for i in range(len(ans1)):
    print(ans1)
    print("value of x[", i + 1, "]=", np, round(ans[i], 2))
