"""
Created on Tue Dec 27 06:08:26 2022

@author: tricialyjun
"""

with open('rockpath', 'r') as f:
    rockpath = [[list(eval(ii)) for ii in jj.split(' -> ')] for jj in f.read().strip().splitlines()]

def rockfinder(rockpath):
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
    return list(set(rockpos))

rock = rockfinder(rockpath)
xmin = min([_[0] for _ in rock])
xmax = max([_[0] for _ in rock])
ymax = max([_[1] for _ in rock])

source = (500, 0)

# Part 1
def falldown(drop, yfloor):
    xpos = drop[0]
    ypos = drop[1]
    while ypos < yfloor:
        down = min([pos[1] for pos in occupied if pos[0] == xpos and pos[1] > ypos]+[yfloor+1])
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

occupied = sorted(rock)
stop = False
while stop != True:
    stop = falldown(source, ymax)

print(len(occupied) - len(rock) - 1)


# Part 2 but it doesn't take forever
extpaths = [[xmin-2, 0], [xmin-2, ymax+2], [xmax+2, ymax+2], [xmax+2, 0]]
rockpath.append(extpaths)
rock2 = rockfinder(rockpath)

occupied = sorted(rock2)
stop = False
while stop != source:
    stop = falldown(source, ymax+2)
    occupied.append(stop)
    print(stop)

areasand = len(occupied) - len(rock2)
leftpoint = 500 - (ymax+1)
rightpoint = 500 + (ymax+1)
leftarea = (xmin-1-leftpoint)*(xmin-leftpoint)/2
rightarea = (rightpoint-xmax-1)*(rightpoint-xmax)/2
print(sum([leftarea, areasand, rightarea]))