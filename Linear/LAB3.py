import matplotlib.pyplot as plt

start=[0,0]
u=[2,2]
v=[1,-1]

fig,ax= plt.subplots(figsize=(5,5))

ax.quiver(start[0],start[1],u[0],u[1],color="r",scale=7)
plt.show()

ax.quiver(start[0],start[1],v[0],v[1],color="b",scale=7)
plt.show()


import matplotlib.pyplot as plt

start=[0,0,0]
u=[2,2,3]
v=[1,-1,4]
w=[3,-1,2]

fig,ax= plt.subplots(figsize=(5,5))


ax = plt.axes(projection='3d')
ax.quiver(start[0], start[1], start[2], u[0], u[1], u[2], color="b")

ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2], color="r")

ax.quiver(start[0], start[1], start[2], w[0], w[1], w[2], color="y")

ax.view_init(0, 10)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
plt.show()



import matplotlib.pyplot as plt
start = [0, 0, 0]
u = [2, 2, 3]
v = [1, -1, 4]
w = [3, -1, 2]
e = [-3, 12, -2]

h = [9, 6, 12]
g = [3, 8, 9]
fig, ax = plt.subplots(figsize=(5, 5))
ax = plt.axes(projection='3d')
ax.quiver(start[0], start[1], start[2], u[0], u[1], u[2], color="b")
ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2], color="r")
ax.quiver(start[0], start[1], start[2], w[0], w[1], w[2], color="y")
ax.quiver(start[0], start[1], start[2], e[0], e[1], e[2], color="y")
ax.quiver(start[0], start[1], start[2], h[0], h[1], h[2], color="g")
ax.quiver(start[0], start[1], start[2], g[0], g[1], g[2], color="b")
ax.view_init(0, 10)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
plt.show()