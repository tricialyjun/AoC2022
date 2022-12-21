"""
Created on Wed Dec 21 02:15:14 2022

@author: tricialyjun
"""

with open("treemap", "r") as f:
    treemap = f.read().strip().split("\n") 

treemap = [[int(xx) for xx in yy] for yy in treemap]

# Part 1
visible = [[False]*99 for _ in range(99)]
for jj in range(1,98):
    westheight  = treemap[jj][0]
    northheight = treemap[0][jj]
    eastheight  = treemap[jj][98]
    southheight = treemap[98][jj]
    for ii in range(1,98):
        # Viewed from west
        if treemap[jj][ii] > westheight:
            visible[jj][ii] = True
            westheight = treemap[jj][ii]
        # Viewed from north    
        if treemap[ii][jj] > northheight:
            visible[ii][jj] = True
            northheight = treemap[ii][jj]
        # Viewed from east    
        if treemap[jj][-1-ii] > eastheight:
            visible[jj][-1-ii] = True
            eastheight = treemap[jj][-1-ii]
        # Viewed from south
        if treemap[-1-ii][jj] > southheight:
            visible[-1-ii][jj] = True
            southheight = treemap[-1-ii][jj]
            
interior = sum([sum([int(xx) for xx in yy]) for yy in visible])
exterior = 98*4
print(str(interior+exterior))

# Part 2
def firstGT(searchList, searchTerm):
    for index, item in enumerate(searchList):
        if item >= searchTerm:
            break
    return index+1
    
scenery = [[0]*99 for _ in range(99)]
treemapNS = list(zip(*treemap))
for jj in range(1,98):
    for ii in range(1,98):
        height = treemap[jj][ii]
        westview  = firstGT(reversed(treemap[jj][:ii]), height)
        eastview  = firstGT(treemap[jj][ii+1:], height)
        northview = firstGT(reversed(treemapNS[ii][:jj]), height)
        southview = firstGT(treemapNS[ii][jj+1:], height)
        scenery[jj][ii] = westview*eastview*northview*southview
        
print(max([max(yy) for yy in scenery]))