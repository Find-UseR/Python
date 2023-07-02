import numpy as np

r = int(input('Enter No. of Rows: '))
c = int(input('Enter No. of Columns: '))
grid = [[0]*c for _ in range(r)]

randRow = np.random.randint(r)
randCol = np.random.randint(c)
grid[randRow][randCol] = 3

if randRow > 0:
    grid[randRow-1][randCol] = 6
if randRow < r-1:
    grid[randRow+1][randCol] = 6
if randCol > 0:
    grid[randRow][randCol-1] = 6
if randCol < c-1:
    grid[randRow][randCol+1] = 6

for i in range(r):
    print(grid[i])
