"""
Created on Wed Dec 21 18:21:58 2022

@author: tricialyjun
"""

# Load input
with open("CPUsignal", "r") as f:
    signal = f.read().strip().split("\n") 

# Part 1
X = 1
cyclelog = [X]
for ii in signal:
    if ii[:4] == 'noop':
        cyclelog.append(X)
    elif ii[:4] == 'addx':
        cyclelog.append(X)
        X += int(ii.split(" ")[-1])
        cyclelog.append(X)

strength = [cyclelog[ii-1]*ii for ii in range(20, 240, 40)]
sum(strength)

# Part 2
screen = [['.']*40 for ii in range(6)]
for jj in range(240):
    sprite = list(range(cyclelog[jj]-1,cyclelog[jj]+2))
    xx = jj%40
    yy = int(jj/40)
    if xx in sprite:
        screen[yy][xx] = '#'

with open("CRToutput", "w") as f:
    for line in screen:
        f.write("".join(line))
        f.write("\n")