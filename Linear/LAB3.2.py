import numpy as np

List1=[10,20,30,40,50]

vtr1=np.array(List1)
print(vtr1)
List2=[ [12],
        [15],
        [17],
        [19]]

vtr2=np.array(List2)
print(vtr2)
vtr1=np.array(List1)
print(vtr1)

List3=[11,12,15,17,20]
('we are creating a vector from list 3')

vtr3=np.array(List3)
print(vtr3)

vtrAdd=vtr1+vtr3
print(vtrAdd)

vtrSub=vtr1-vtr3
print(vtrSub)

vtrMul=vtr1*vtr3
print(vtrMul)

vtrProd=vtr1.dot(vtr3)
print(vtrProd)

scalarValue =6
print('Any scalar multiplication with vector')

vtrScl=vtr1*scalarValue
print(vtrScl)




