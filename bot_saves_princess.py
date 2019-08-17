#!/usr/bin/python

def findPositions(n, grid):
    m = []
    p = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                m.append(i)
                m.append(j)
            if grid[i][j] == 'p':
                p.append(i)
                p.append(j)
    return m, p

def displayPathtoPrincess(n,grid):
    m, p = findPositions(n, grid)
    x_dist = m[0] - p[0]
    y_dist = m[1] - p[1]
    if x_dist > 0:
        for i in range(x_dist):
            print('UP')
    else:
        for i in range(abs(x_dist)):
            print('DOWN')
    
    if y_dist > 0:
        for i in range(y_dist):
            print('LEFT')
    else:
        for i in range(abs(y_dist)):
            print('RIGHT')
    
                
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)