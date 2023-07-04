#Code for checking given vector is in span of S(set of vectors) or not
#where  S is also given
import numpy as np
import math
a=eval(input("Input size Of the square Coeffecient matrix"))
c=1
matrix=[] #list
vector=[] #constant vector
for i in range(a):   #column
    r=1
    column=[]
    for i in range(a):  #rows
        print("Enter value of column", c)
        x=eval(input())
        column.append(x) #add element at the end of the list
        r=r+1
    c=c+1
    matrix.append(column)
    print("Your column=", matrix)
matrix=np.asarray(matrix)
print("Your original matrix=" , matrix)
matrix=np.transpose(matrix)
print("Your required matrix=", matrix)
for i in range(a):
    print("Enter Your value of given vector ", i+1)
    x=eval(input())
    vector.append(x)
v1=np.asarray(vector)
new_vector=[]
for i in vector:
    new_vector.append([i])
new_vector=np.array(new_vector)    #convert list into array
aug=np.append(matrix,new_vector,axis=1)
print("Your Augmented matrix=", aug)
            ##########################
def row_interchange(mat,row1,row2):
    t1=mat[row1].copy()
    t2=mat[row2].copy()
    mat[row1]=t2
    mat[row2]=t1
    return mat
                   ####################
def scalar_multiply(mat,scalar):
    return mat * scalar
                 ###############################
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

count=0
for i in ans2:
    if i==math.inf or i==math.nan:
        print("Your Given Vector is Not in span of set")
        break
    elif i!=math.inf or i!=math.nan:
        count+=1
if count==a:
    print("Your Given Vector is in span of set")


