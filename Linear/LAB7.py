import numpy as np

a = np.array([[2, 3, 4, 34],
             [5, 6, 7, 45],
             [8, 9, 23, 67],
             [43, 55, 21, 80]])
print(a)

inv = np.linalg.inv(a)
print(inv)
det = np.linalg.det(a)
print(det)
vtr = np.array([[2], [43], [55], [23]])
print(vtr)
ans = np.dot(inv, vtr)
print("Ans  \n", ans)

