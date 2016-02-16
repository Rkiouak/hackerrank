#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    mLoc, pLoc = findBotAndPrincess(grid)
    while(mLoc[0]!=pLoc[0] and mLoc[1]!=pLoc[1]):
        #print(mLoc)
        #print(pLoc)
        if mLoc[0]>pLoc[0]:
            print('LEFT')
            mLoc[0]+=-1
        if mLoc[0]<pLoc[0]:
            print('RIGHT')
            mLoc[0]+=1
        if mLoc[1]<pLoc[1]:
            print('DOWN')
            mLoc[1]+=1
        if mLoc[1]>pLoc[1]:
            print('UP')
            mLoc[1]+=-1
    
def findBotAndPrincess(grid):
    mLoc=[-1, -1]
    pLoc=[-1, -1]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='m':
                   mLoc=[j, i]
            if grid[i][j]=='p':
                   pLoc=[j, i]

    return [mLoc, pLoc]
    
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

