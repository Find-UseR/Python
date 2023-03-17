import numpy as np

a = eval(input("Enter the number= "))
print("Number is: ", a)
i = 1
while i <= a:
    print(i, 'My Name is Aqib')
    i = i + 1

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
print("Coefficient matrix= ", m)
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
