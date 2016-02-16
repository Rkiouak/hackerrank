#
def nextMove(n,r,c,grid):
    mLoc = [c, r]
    pLoc=findPrincess(grid)
    if mLoc[0]>pLoc[0]:
        return 'LEFT'
    if mLoc[0]<pLoc[0]:
        return 'RIGHT'
    if mLoc[1]<pLoc[1]:
        return 'DOWN'
    if mLoc[1]>pLoc[1]:
        return 'UP'

def findPrincess(grid):
    pLoc=[-1, -1]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='p':
                   pLoc=[j, i]

    return pLoc
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

