"""
Created on Thu Dec 29 13:43:41 2022

@author: tricialyjun
"""
with open('sensormap', 'r') as f:
    sensormap = f.read().strip().split('\n')

sensormap = [''.join([jj for jj in ii if jj.isnumeric() or jj in ['-',',',':']]) for ii in sensormap]
sensors = [tuple([int(ll) for ll in kk.split(':')[0].split(',')]) for kk in sensormap]
beacons = [tuple([int(ll) for ll in kk.split(':')[1].split(',')]) for kk in sensormap]

def mandist(a, b):
    distance = abs(b[0]-a[0]) + abs(b[1]-a[1])
    return distance

# Part 1
def voidrow(origin, distance, row):
    rowdist = row - origin[1]
    west = origin[0] - (distance - abs(rowdist))
    east = origin[0] + (distance - abs(rowdist))
    horz = list(range(west, east+1))
    vert = [row]*len(horz)
    void = list(zip(horz, vert))
    return void

row = 2000000
voidlist = []
for vv in range(len(sensors)):
    distance = mandist(sensors[vv], beacons[vv])
    if row in range(sensors[vv][1]-distance,sensors[vv][1]+distance+1):
        voidlist += voidrow(sensors[vv], distance, row)
voidlist = list(set(voidlist))
voidsize = len([ll for ll in voidlist if (ll not in beacons) and (ll not in sensors)])
print(voidsize)

# Part 2
# clockwise
# - 1/\2 +
# + 4\/3 -

def perimlines(origin, distance):
    # c = y - mx
    c1 = origin[1] + (origin[0]-(distance+1))
    c2 = origin[1] - (origin[0]+(distance+1))
    c3 = origin[1] + (origin[0]+(distance+1))
    c4 = origin[1] - (origin[0]-(distance+1))
    return c1, c2, c3, c4

def intersect(cneg, cpos):
    # x + cp = -x + cn
    x = (cneg - cpos)/2
    y = x + cpos
    return x, y

posmin = 0
posmax = 4000000
negslope = []
posslope = []
for vv in range(len(sensors)):
    distance = mandist(sensors[vv], beacons[vv])
    c1, c2, c3, c4 = perimlines(sensors[vv], distance)
    negslope += [c1] + [c3]
    posslope += [c2] + [c4]

negshort = [nn for nn in set(negslope) if negslope.count(nn) > 1]
posshort = [pp for pp in set(posslope) if posslope.count(pp) > 1]

intersections = []
for nn in negshort:
    for pp in posshort:
        x, y = intersect(nn, pp)
        if x >= posmin and x <= posmax and y >= posmin and y <= posmax and x == int(x) and y == int(y):
            intersections.append((int(x), int(y)))

yshort = set([y[1] for y in intersections])
for rr in yshort:
    voidlist = []
    for vv in range(len(sensors)):
        distance = mandist(sensors[vv], beacons[vv])
        if rr in range(sensors[vv][1]-distance, sensors[vv][1]+distance+1):
            voidlist += voidrow(sensors[vv], distance, rr)
    voidlist = list(set(voidlist))
    voidxset = [ll[0] for ll in voidlist if ll[0] >= posmin and ll[0] <= posmax]
    if len(voidxset) < posmax+1:
        xpos = list(set(range(posmax+1)) - set(voidxset))
        ypos = rr
        break

print(xpos[0]*posmax+ypos)