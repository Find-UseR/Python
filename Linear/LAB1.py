import numpy as n
arr=n.array([1, 2, 3, 4 , 5])
print(arr)

arnge=n.arange(-34,6,.6)
print(arnge)

oncmatrix=n.ones((5,9),dtype=int)
print(oncmatrix)

zeematrix=n.zeros((3,7),dtype=int)
print(zeematrix)

matrix=n.array([[-1,3,2], [3,4,1], [8,9,7]])
print(matrix)

dia=n.dign(matrix)
print(dia)

index=matrix[0][1]
print(index)

lst=[4, 5.6, 'My name is Aqib', 7,8]
print(lst)

ind=lst[1:4]
print(ind)

row= matrix[2]
print(row)

column= matrix[:,2]
print(column)

ls= n.linspace(2,20,60)
print(ls)
