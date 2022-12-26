"""
Created on Sun Dec 25 23:53:00 2022

@author: tricialyjun
"""
def signaldepth(signal):
    currdepth = [[[len(signal)]]]
    while set([_[-1][0] for _ in currdepth]) != {0}:
        nextdepth = []
        for ii in currdepth:
            if ii[-1][0] != 0:
                for jj in range(ii[-1][0]):
                    index  = ii[:-1] + [[jj]]
                    posval = eval('signal'+''.join([str(_) for _ in index]))
                    if type(posval) == list:
                        nextdepth.append(index + [[len(posval)]])
                    elif type(posval):
                        nextdepth.append(index + [[0]])
            else:
                nextdepth.append(ii)
        currdepth = nextdepth
    currdepth = [_[:-1] for _ in currdepth]
    return currdepth

def matchdepth(leftdepth, rightdepth):
    depthdiff = len(leftdepth) - len(rightdepth)
    if depthdiff > 0:
        leftmatch  = leftdepth
        rightmatch = rightdepth + [[0]]*abs(depthdiff)
    elif depthdiff < 0:
        leftmatch  = leftdepth + [[0]]*abs(depthdiff)
        rightmatch = rightdepth
    else:
        leftmatch  = leftdepth
        rightmatch = rightdepth
    lstring = ''.join([str(_[0]) for _ in leftmatch])
    rstring = ''.join([str(_[0]) for _ in rightmatch])
    return lstring, rstring

def comparelr(ldepth, rdepth, counter):
    if counter < min(len(ldepth),len(rdepth)):
        lmatch, rmatch = matchdepth(ldepth[counter], rdepth[counter])
        if lmatch == rmatch:
            lcheck = eval('left'+''.join([str(_) for _ in ldepth[counter]]))
            rcheck = eval('right'+''.join([str(_) for _ in rdepth[counter]]))
            if lcheck == rcheck == []:
                lcheck = len(ldepth[counter])
                rcheck = len(rdepth[counter])
            elif type(lcheck) != type(rcheck):
                if type(lcheck) == int:
                    lcheck = [lcheck]
                elif type(rcheck) == int:
                    rcheck = [rcheck]
        elif lmatch < rmatch:
            lcheck = 1
            rcheck = 0
        elif lmatch > rmatch:
            lcheck = 0
            rcheck = 1
    else:
        lcheck = len(ldepth)
        rcheck = len(rdepth)   
    return lcheck, rcheck

# Part 1
with open("distress", "r") as f:
    distress = f.read().strip().split("\n\n")

ordered = []
for ii in range(len(distress)):
    left   = eval(distress[ii].split('\n')[0])
    right  = eval(distress[ii].split('\n')[1])
    ldepth = signaldepth(left)
    rdepth = signaldepth(right)
    for jj in range(max(len(ldepth),len(rdepth))):
        lcheck, rcheck = comparelr(ldepth, rdepth, jj)
        if lcheck < rcheck:
            ordered.append(ii+1)
            break
        elif lcheck > rcheck:
            break
        else:
            continue
    
print(sum(ordered))

# Part 2
with open("distress", "r") as f:
    distress_all = [eval(x) for x in f.read().strip().replace("\n\n","\n").split("\n")]+[[[2]]]+[[[6]]]

ordered = 0
while ordered < len(distress_all):
    ordered = 1
    for kk in range(1,len(distress_all)):
        left = distress_all[kk-1]
        right = distress_all[kk]
        ldepth = signaldepth(left)
        rdepth = signaldepth(right)
        for ll in range(max(len(ldepth),len(rdepth))):
            lcheck, rcheck = comparelr(ldepth, rdepth, ll)
            if lcheck < rcheck:
                ordered += 1
                break
            elif lcheck > rcheck:
                distress_all.insert(kk-1, distress_all.pop(kk))
                break
            else:
                continue

print((distress_all.index([[2]])+1)*(distress_all.index([[6]])+1))