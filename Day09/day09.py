"""
Created on Wed Dec 21 14:59:41 2022

@author: tricialyjun
"""

# Functions
def roundout(value):
    if abs(value - int(value)) < 0.5:
        return int(value)
    else:
        sign = value/abs(value)
        return (abs(int(value))+1)*sign

def trajectory(head, tail):
    mv_x, mv_y = 0, 0
    xdist = head[0]-tail[0]
    ydist = head[1]-tail[1]
    dist = (xdist**2+ydist**2)**0.5
    if dist >= 2:
        mv_x = int(roundout(xdist/2))
        mv_y = int(roundout(ydist/2))
    return mv_x, mv_y

def movehead(head, direction):
    if direction == 'L':
        head[0] -= 1
    elif direction == 'R':
        head[0] += 1
    elif direction == 'D':
        head[1] -= 1
    elif direction == 'U':
        head[1] += 1 

# Load input
with open("ropemovement", "r") as f:
    mvmt = f.read().strip().split("\n") 

headmvmt = []
for hh in mvmt:
    direction = hh.split(" ")[0]
    steps     = int(hh.split(" ")[-1])
    headmvmt += [direction] * steps

# Part 1
### Initiate x, y coordinates
head = [0, 0]   
tail = [0, 0]
tailhistory = ['0 0']
for tt in headmvmt:
    movehead(head, tt)
    mv_x, mv_y = trajectory(head, tail)
    tail[0], tail[1] = tail[0]+mv_x, tail[1]+mv_y
    tailhistory.append(str(tail[0]) +' ' + str(tail[1]))

len(set(tailhistory))

# Part 2
### Initiate x, y coordinates
rope = [[0, 0] for _ in range(10)] 
tailhistory = ['0 0']
for tt in headmvmt:
    movehead(rope[0], tt)
    for rr in range(1,10):
        mv_x, mv_y = trajectory(rope[rr-1], rope[rr])
        rope[rr][0] += mv_x
        rope[rr][1] += mv_y 
    tailhistory.append(str(rope[9][0]) +' ' + str(rope[9][1]))

len(set(tailhistory))