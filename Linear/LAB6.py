#Code for solving nxn system of linear eqns 
by
#Guass Elimination Method
import numpy as np
a=eval(input("Input the size of the square 
matrix? "))
r=1
matrix=[]
vector=[]
for i in range(a):
 c=1
 row=[]
 for i in range(a):
 print("Enter value of row 
",r,"column ",c)
 x=eval(input())
 row.append(x)
 c=c+1
 matrix.append(row)
 print("Enter constant value of equation 
",r)
 x=eval(input())
 vector.append(x)
 r=r+1
m=np.asarray(matrix)
v1=np.asarray(vector)
print("Your Square Matrix=\n", m)
print("Your constant Vector= \n",v1)
aug=np.copy(m)
new_v1=[]
for i in v1:
 new_v1.append([i])
new_v1=np.asarray(new_v1)
print("Your column vector= \n",new_v1)
aug=np.append(aug,new_v1,axis=1)
print("Your final Augumented Matrix =\n "
, 
aug)
############# Scalar Mutliplication######
def slr_mul (mat,s1):
 return mat*s1
############# addition two rows#########
def row_add (mat,vect,rownum):
 mat[rownum]=mat[rownum]+vect
 return mat
for i in range(0,a):
 for j in range(i+1,a):
 ratio=aug[j][i]/aug[i][i]
 mul_result=slr_mul(aug[i],ratio)
 print("Mutliplication result= 
",mul_result)
 aug=row_add(aug,-mul_result,j)
 print("Your Augumnet result 
is\n",aug)
# Back substitution
ans1=np.zeros(a)
ans1[a-1]=aug[a-1][a]/aug[a-1][a-1]
for i in range(a-2,-1,-1):
 ans1[i]=aug[i][a]
 for j in range(i+1,a):
 ans1[i]=ans1[i]-aug[i][j]*ans1[j]
 ans1[i]=ans1[i]/aug[i][i]
for i in range(len(ans1)):
 print("Value of 
x[",i+1,"]=",np.round(ans1[i],2),end='\t')