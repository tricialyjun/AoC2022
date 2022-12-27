"""
Created on Tue Dec 27 02:17:11 2022

@author: tricialyjun
"""
with open('rockpath', 'r') as f:
    rockpath = [[list(eval(ii)) for ii in jj.split(' -> ')] for jj in f.read().strip().splitlines()]

rockpos = []
for positions in rockpath:
    for jj in range(1,len(positions)):
        init = positions[jj-1]
        finl = positions[jj]
        if init[0] == finl[0]:
            # Movement in y direction
            yy = list(range(min(init[1],finl[1]),max(init[1],finl[1])+1))
            xx = [init[0]]*len(yy)
        elif init[1] == finl[1]:
            # Movement in x direction
            xx = list(range(min(init[0],finl[0]),max(init[0],finl[0])+1))
            yy = [init[1]]*len(xx)
        [rockpos.append((x, y)) for x, y in list(zip(xx,yy))]

rockpos = list(set(rockpos))
xmin = min([_[0] for _ in rockpos])
xmax = max([_[0] for _ in rockpos])
ymax = max([_[1] for _ in rockpos])

source = (500, 0)

# Part 1
def falldown(drop):
    xpos = drop[0]
    ypos = drop[1]
    while (xpos > xmin) and (xpos < xmax) and (ypos < ymax):
        down = min([pos[1] for pos in occupied if pos[0] == xpos and pos[1] > ypos]+[ymax+1])
        if (xpos-1, down) not in occupied:
            xpos = xpos-1
            ypos = down
        elif (xpos+1, down) not in occupied:
            xpos = xpos+1
            ypos = down
        else:
            stop = (xpos, down-1)
            return stop
    return True

occupied = sorted(rockpos)
stop = False
while stop != True:
    stop = falldown(source)
    occupied.append(stop)

print(len(occupied) - len(rockpos) - 1)

    
# Part 2
def falldown2(drop):
    xpos = drop[0]
    ypos = drop[1]
    while ypos < yfloor:
        down = min([pos[1] for pos in occupied if pos[0] == xpos and pos[1] > ypos]+[yfloor])
        if down == yfloor:
            stop = (xpos, down-1)
            return stop
        elif(xpos-1, down) not in occupied:
            xpos = xpos-1
            ypos = down
        elif (xpos+1, down) not in occupied:
            xpos = xpos+1
            ypos = down
        else:
            stop = (xpos, down-1)
            return stop
    return True

occupied = sorted(rockpos)
yfloor = ymax+2
while stop != source:
    stop = falldown2(source)
    occupied.append(stop)

len(set(occupied)) - len(rockpos)
# 28744