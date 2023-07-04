# Code for  A=L * U decomposition of n*n system of linear Equations
import numpy as np

a = eval(input("Input size of the  Square Cofficient Matrix : "))
r = 1
matrix = []
vector = []
for i in range(a):
    c = 1
    row = []
    for i in range(a):
        print("Enter value of row", r, "Column", c)
        x = eval(input())
        row.append(x)
        c = c + 1
    matrix.append(row)
    print("Enter constant of equation", r)
    x = eval(input())
    vector.append(x)
    r = r + 1
m = np.asarray(matrix)
print("Cofficient Matrix", m)
n = np.asarray(matrix)  # For Displaying Purpose in the end only
print("Size of Matrix", m.shape)
vector = np.asarray(vector)
aug = np.copy(m)
new_vector = []
for i in vector:  # vector[5,6].....[[5],[6]]
    new_vector.append([i])
new_vector = np.array(new_vector)  # Converting list into array
print("New Vector is: ", new_vector)


def row_interchange(mat, row1, row2):
    t1 = mat[row1].copy()
    t2 = mat[row2].copy()
    mat[row1] = t2
    mat[row2] = t1
    return mat


def scalar_multiply(mat, scalar):
    return mat * scalar


def row_addition(mat, vect, rownum):
    mat[rownum] = mat[rownum] + vect
    return mat


L = np.eye(a)  # This is used
# for creating an Identity Matrix
print("Your Identity Matrix of order", a, "x", a, "=", L)

for i in range(0, a):
    for j in range(i + 1, a):
        if m[i][i] == 0:
            m = row_interchange(m, i, j)
        else:
            ratio = m[j][i] / m[i][i]
            L[j][i] = np.round(ratio, 2)
            mul_result = scalar_multiply(m[i], np.round(ratio, 2))
            print("Multiplication Result", mul_result)
            U = row_addition(m, -mul_result, j)
            print("My new Upper Matrix is= \n", U)
            print("My new Lower Matrix is= \n", L)
mul = np.dot(L, U)  # verifying A is decomposed correctly into "L" and "U"
print("Our Verifying Matrix  L*U is=", mul)
print("Our orignal Matrix A was= ", n)
aug1 = np.append(L, new_vector, axis=1)
print("Augumented Matrix is", aug1)

# Forward Substitution

ans1 = np.zeros(a)
for i in range(a + 1):  # last limit always skips 1 to 3
    if i == a:
        break
    pro = 0
    tmp = aug1[i][a]  # [0,3],...[1,3]...[2,3]...[3.3]]
    for j in range(i):  # 0...0,1....0,1,2
        print("i=", i, "j=", j)
        pro += aug1[i][j] * ans1[j]
        print("pro=", pro)
    tmp = tmp - pro
    ans1[i] = tmp
    print("y is= ", ans1[i])
for i in range(len(ans1)):
    print("value of y[", i + 1, "]=", np.round(ans1[i], 2), end='\t')
new_vector2 = []
for i in ans1:  # vector[5,6]....[[5],[6]]
    new_vector2.append([i])

new_vector2 = np.array(new_vector2)  # Convert list into array
print("New Vector 2 is= ", new_vector2)

aug2 = np.append(U, new_vector2, axis=1)
print("Your Ux= ", aug2)

# Back Substitution
ans2 = np.zeros(a)
ans2[a - 1] = aug2[a - 1][a] / aug2[a - 1][a - 1]
for i in range(a - 2, -1, -1):
    ans2[i] = aug2[i][a]
    for j in range(i + 1, a):
        ans2[i] = ans2[i] - aug2[i][j] * ans2[j]
    ans2[i] = ans2[i] / aug2[i][i]
for j in range(len(ans2)):
    print("value of x[", j + 1, "]=", np.round(ans2[j], 2), end='\t')

