# code for translation and rotation transformation

import numpy as np
import matplotlib.pyplot as plt

# FOR ARROW
# x = [5, 5, 4, 8, 13, 11, 11]
# y = [0, 3, 3, 8, 3, 3, 0]

# FOR CAR
x = [2, 14, 14, 12, 12, 5, 5, 1]
y = [1, 1, 2, 2, 3, 3, 2, 2]
plt.fill(x, y, "RED", alpha=0.3)
# Create Translation Matrix
tx = 2
ty = -1
T = np.array([[1, tx], [0, ty]])
# translate tx and ty units
points_translated_x = []
points_translated_y = []
print("Translated Matrix=", T)
print("Your ist=", x, y)
for i in range(len(x)):
    p_t = np.dot(T, [x[i], y[i]])
    points_translated_x.append(p_t[0])
    print("New x= ", p_t[0])
    points_translated_y.append(p_t[1])
    print("New y= ", p_t[1])
plt.fill(points_translated_x, points_translated_y, "BLUE", alpha=0.2)
# Create Rotation Matrix
theta = np.pi
R = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
# Rotation x and y units
points_rotation_x = []
points_rotation_y = []
for i in range(len(x)):
    p_r = np.dot(R, [x[i], y[i]])
    points_rotation_x.append(p_r[0])
    print("New x= ", p_r[0])
    points_rotation_y.append(p_r[1])
    print("New y= ", p_r[1])
plt.fill(points_rotation_x, points_rotation_y, "yellow", alpha=0.6)

plt.show()
