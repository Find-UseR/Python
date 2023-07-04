#Code for checking Linealry Independent or Linearly Dependent vector space
import numpy as np
a=eval(input("Enter size f the square coeffecient matrix"))
c=1
matrix=[] #List
vector=[] #Constant vector
for i in range(a):   #column
    r=1
    column=[]
    for i in range(a): #rows
        print("Enter value of column ", c)
        x=eval(input())
        column.append(x)  # add an element at the end of list
        r=r+1
    c=c+1
    matrix.append(column)
    print("Your Column= ", matrix)
matrix=np.asarray(matrix)
print("Your Matrix Original= ", matrix)
matrix=np.transpose(matrix)
print("Required Matrix= ", matrix)
vector=np.zeros(a)  # To insert zero vector on right side like Ax=0
print("Vector is= ", vector)
new_vector=[]
for i in vector:   #vector[5,6]....[[5],[6]]
    new_vector.append([i])
new_vector=np.array(new_vector) #converting list into array
aug=np.append(matrix,new_vector,axis=1)   #axis=0 .. add row, axis=1 .. add column
print("Your Augumented matrix with zero's= ", aug)


def row_interchange(mat,row1,row2):
    t1=mat[row1].copy()
    t2=mat[row2].copy()
    mat[row1]=t2
    mat[row2]=t1
    return mat

def scalar_multiply(mat,scalar):
    return mat * scalar

def row_addition(mat,vect,rownum):
    mat[rownum]=mat[rownum]+vect
    return mat

for i in range(0,a):
    for j in range(i+1,a):
                #for pivot and making zeros
        ratio=aug[j][i]/ aug[i][i]
        mul_result=scalar_multiply(aug[i],ratio)
        print("Multpilaction Result= ", mul_result)
        aug=row_addition(aug,-mul_result,j)
        print("Your Augumented Result is= \n", aug)

                         #Back Substituion
ans2=np.zeros(a)
ans2[a-1]=aug[a-1][a]/aug[a-1][a-1]
for i in range(a-2,-1,-1):
    ans2[i]=aug[i][a]
    for j in range(i+1,a):
        ans2[i]=ans2[i]-aug[i][j]*ans2[j]
    ans2[i]=ans2[i]/aug[i][i]
for j in range(len(ans2)):
    print("value of x[", j + 1, "]=", np.round(ans2[j], 2))
if ans2.all()==0:
    print("Your Given vectors from space ", a, "X", a,"= Linearly Independent")
else:
    print("Your Given vectors from space ", a, "X", a, "= Linearly Dependent")