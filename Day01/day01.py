"""
Created on Thu Dec  1 22:40:08 2022

@author: tricialyjun
"""

with open('calories', 'r') as f:
    inventories = f.read().split("\n\n")

total_calories = []
for ii in range(len(inventories)):
    curr_inventory = [int(x) for x in inventories[ii].rstrip('\n').split("\n")]
    total_calories.append(sum(curr_inventory))

print(max(total_calories))

total_calories.sort(reverse=True)
print(sum(total_calories[0:3]))