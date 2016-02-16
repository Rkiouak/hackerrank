#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
    mLoc = [posr, posc]
    if board[posr][posc]=='d':
        answer='CLEAN'
    else:
        pLoc=findClosestDirty(mLoc, board)
        #print(pLoc)
        #print('mLoc: '+str(mLoc))
        if mLoc[1]>pLoc[1]:
            answer='LEFT'
        if mLoc[1]<pLoc[1]:
            answer='RIGHT'
        if mLoc[0]<pLoc[0]:
            answer='DOWN'
        if mLoc[0]>pLoc[0]:
            answer='UP'
    print(answer)

def findClosestDirty(mLoc, grid):
    dirtyLocs = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='d':
                dirtyLocs.append([i,j])
    closest=[99999999,[999999,999999]]
    for loc in dirtyLocs:
        distance=(abs(mLoc[0]-loc[0])+abs(mLoc[1]-loc[1]))
        if distance<closest[0]:
            closest[0]=distance
            closest[1]=loc
    return closest[1]


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
