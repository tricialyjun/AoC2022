"""
Created on Fri Dec 30 23:50:23 2022

@author: tricialyjun
"""
with open('valvepressure', 'r') as f:
    valvepressure = f.read().strip().splitlines()
 
valve = {}
for _ in valvepressure:
    valve[_[6:8]] = {}
    valve[_[6:8]]['rate'] = int(_[23:25].strip(';'))
    valve[_[6:8]]['path'] = _[49:].strip().split(', ')

points = [k for k in valve.keys() if valve[k]['rate'] > 0]

def shortestpath(point1, point2):
    pathhistory = []
    currpos     = [point1]
    pathlength  = 1
    while point2 not in pathhistory:
        pathlength +=1
        newpos = []
        for pp in currpos:
            nextpos = valve[pp]['path']
            for nn in nextpos:
                if nn not in pathhistory:
                    pathhistory.append(nn)
                    newpos.append(nn)
        currpos = newpos
    return pathlength

def maxpressure(nodes, initnode, maxcost):
    paths = {}
    paths['0'] = {'history': [initnode], 'tcost': 0, 'pressure': 0}
    
    for jj in range(len(nodes)):
        new = {}
        cc = 0
        for pp in paths:
            currpos = paths[pp]['history'][-1]
            pointsleft = set(nodes) - set(paths[pp]['history'])
            for ll in pointsleft:
                totalcost = paths[pp]['tcost']+ shortestpath(currpos, ll)
                if totalcost <= maxcost:
                    new[str(cc)] = {}
                    new[str(cc)]['history'] = paths[pp]['history'][:]
                    new[str(cc)]['history'].append(ll)
                    new[str(cc)]['tcost'] = totalcost
                    new[str(cc)]['pressure'] = paths[pp]['pressure']+(maxcost-totalcost)*valve[ll]['rate']
                    cc += 1
                    
        if cc == 0:
            break
        else:
            paths = new
            
    return max([paths[_]['pressure'] for _ in paths])

# Part 1
print(maxpressure(points, 'AA', 30))

# Part 2
def samplen(array, n):
    sz = len(array)
    c = list(range(n))
    sample = [[array[_] for _ in c]]
    i = n-1
    while i >= 0:
        if c[i] < sz+i-n:
             c[i] += 1
             if i != n-1:
                 c[i+1:] = range(c[i]+1, c[i]+n-i)
                 i = n-1
             sample.append([array[_] for _ in c])
        else:
             i = i-1
    return sample

tt = 0
totalpressure = {}
sample = samplen(points, int(len(points)/2)) # Highest pressure most likely when paths are about evenly split, but a for loop could be used to try different split sizes
for s1 in sample:
    s2 = list(set(points)-set(s1))
    pressure1 = maxpressure(s1, 'AA', 26)
    pressure2 = maxpressure(s2, 'AA', 26)
    tp = pressure1+pressure2
    print(', '.join(s1)+ ' | '+ ', '.join(s2) + ' = ' + str(tp))
    if tp > 2000:
        totalpressure[str(tt)] = {'s1': s1, 's2': s2, 'tp': pressure1+pressure2}
        tt+=1
        
maxsplitpath = max([totalpressure[_]['tp'] for _ in totalpressure]) 
print(maxsplitpath)

