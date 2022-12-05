"""
Created on Mon Dec  5 13:28:43 2022

@author: tricialyjun
"""

with open("cratemovement", "r") as f:
    crate = [next(f) for _ in range(8)]
    [next(f) for _ in range(2)]
    movement = [next(f).strip().replace("move ", "").replace("from ","").replace("to ","").split(" ") for _ in range(503)]

crate_T = list(zip(*crate))[1::4]

# Part 1
crate_list = [[y for y in x if y != " "] for x in crate_T]
for ii in range(len(movement)):
    for jj in range(int(movement[ii][0])):
        crane = crate_list[int(movement[ii][1])-1].pop(0)
        crate_list[int(movement[ii][2])-1].insert(0,crane)
print("".join([x[0] for x in crate_list]))

# Part 2
crate_list_2 = [[y for y in x if y != " "] for x in crate_T]
for ii in range(len(movement)):
    crane = []
    for jj in range(int(movement[ii][0])):
        crane.append(crate_list_2[int(movement[ii][1])-1].pop(0))
    crate_list_2[int(movement[ii][2])-1] = crane + crate_list_2[int(movement[ii][2])-1] 
print("".join([x[0] for x in crate_list_2]))