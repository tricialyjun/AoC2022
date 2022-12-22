"""
Created on Thu Dec 22 02:30:21 2022

@author: tricialyjun
"""
with open("elevationmap", "r") as f:
    elevmap = f.read().strip().split("\n")

### Get Row and Columns of Position
startpos = [(elevmap.index(yy), yy.index('S')) for yy in elevmap if 'S' in yy][0]
endpos = [(elevmap.index(yy), yy.index('E')) for yy in elevmap if 'E' in yy][0]
elevmap = [[ord(xx) for xx in yy.replace('S','a').replace('E','z')] for yy in elevmap]

def regionsearch(currpos):
    posy, posx = currpos[0], currpos[1]
    o = elevmap[posy][posx]
    nextpos = []
    if (posy != 0) and (o - elevmap[posy-1][posx] < 2):
        nextpos.append((posy-1, posx))
    if (posy != 40) and (o - elevmap[posy+1][posx] < 2):
        nextpos.append((posy+1, posx))
    if (posx != 0) and (o - elevmap[posy][posx-1] < 2):
        nextpos.append((posy, posx-1))
    if (posx != 160) and (o - elevmap[posy][posx+1] < 2):
        nextpos.append((posy, posx+1))
    return nextpos

# Part 1
paths = {}
paths['0'] = {}
paths['0']['history'] = [endpos]
pathhistory = [endpos];

while startpos not in pathhistory:
    newpaths = {}
    pathcounter = 0
    for jj in paths:
        currpos = paths[jj]['history'][-1]
        nextpos = regionsearch(currpos)
        for ii in nextpos:
            if ii not in pathhistory:
                newpaths[str(pathcounter)] = {}
                newpaths[str(pathcounter)]['currval'] = chr(elevmap[ii[0]][ii[1]])
                newpaths[str(pathcounter)]['history'] = paths[jj]['history'][:]
                newpaths[str(pathcounter)]['history'].append(ii)
                pathhistory.append(ii)
                pathcounter += 1
    paths = newpaths

print(len(paths['0']['history'])-1)

# Part 2
paths = {}
paths['0'] = {}
paths['0']['history'] = [endpos]
paths['0']['currval'] = 'z'
pathhistory = [endpos];
allcurrval = [value['currval'] for value in paths.values()]

while 'a' not in allcurrval:
    newpaths = {}
    pathcounter = 0
    for jj in paths:
        currpos = paths[jj]['history'][-1]
        nextpos = regionsearch(currpos)
        for ii in nextpos:
            if ii not in pathhistory:
                newpaths[str(pathcounter)] = {}
                newpaths[str(pathcounter)]['currval'] = chr(elevmap[ii[0]][ii[1]])
                newpaths[str(pathcounter)]['history'] = paths[jj]['history'][:]
                newpaths[str(pathcounter)]['history'].append(ii)
                pathhistory.append(ii)
                pathcounter += 1
    paths = newpaths
    allcurrval = [value['currval'] for value in paths.values()]

print(len(paths['0']['history'])-1)