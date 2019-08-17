#
def findPrincess(n, grid):
    p = list()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                p.append(i)
                p.append(j)
    return p

def nextMove(n,r,c,grid):
    p = findPrincess(n, grid)
    r_dist = r - p[0]
    c_dist = c - p[1]
    
    next = None
    if r_dist > 0:
        next = 'UP'
    elif r_dist < 0:
        next = 'DOWN'
    
    if c_dist > 0:
        next = 'LEFT'
    elif c_dist < 0:
        next = 'RIGHT'
    
    return next

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))