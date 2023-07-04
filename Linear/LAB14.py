 # CODE FOR DIFFERENT TRANSFORMATIONS

import numpy as np
import matplotlib.pyplot as plt

x = [-9, -9, -10, -10, -7, -7, -7, -6, -6, -7, -7, -4, -4, -5, -5, -4, -4, -5, -5, -4, -4, -2, -2, -5, -5, -6, -6, -8,
     -8, -9]
y = [-2, 0, 0, 3, 3, 6, 7, 7, 6, 6, 7, 7, 7, 7, 7, 6, 6, 7, 6, 6, 3, 3, 0, 0, -2, -2, 0, 0, -2, -2]

print("length of x is: ", len(x))
print("length of y is: ", len(y))

x = np.asarray(x)
y = np.asarray(y)

plt.fill(x, y, color="RED", alpha=0.7)
plt.scatter(x, y, color="BLUE", alpha=1)

plt.xticks(np.arange(-30, 30, 1))
plt.yticks(np.arange(-30, 30, 1))

# T=np.array([[-1,0],[0,1]])   #reflection along y-axis
# T=np.array([[1,0],[0,-1]])   #reflection along x-axis
T = np.array([[-1, 0], [0, -1]])  # reflection along origin
# T=np.array([[0,1],[1,0]])   #reflection along y=x
# T=np.array([[0,-1],[-1,0]])   #reflection along y=-x

new_points_x = []
new_points_y = []

for i in range(len(x)):
    p_t = np.dot(T, [x[i], y[i]])
    new_points_x.append(p_t[0])
    new_points_y.append(p_t[1])
plt.fill(new_points_x, new_points_y, "Green", alpha=1)
plt.grid(color="Black", linestyle="-.", linewidth=0.4)
plt.show()
