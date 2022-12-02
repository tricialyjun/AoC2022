"""
Created on Thu Dec  1 22:40:08 2022

@author: tricialyjun
"""

<<<<<<< HEAD
=======
# Part 1
>>>>>>> 643b2bbafb19c9e46fe5be73ad59e668578e2aa5
with open('calories', 'r') as f:
    inventories = f.read().split("\n\n")

total_calories = []
for ii in range(len(inventories)):
    curr_inventory = [int(x) for x in inventories[ii].rstrip('\n').split("\n")]
    total_calories.append(sum(curr_inventory))

<<<<<<< HEAD
# Part 1
=======
>>>>>>> 643b2bbafb19c9e46fe5be73ad59e668578e2aa5
print(max(total_calories))

# Part 2
total_calories.sort(reverse=True)
<<<<<<< HEAD
print(sum(total_calories[0:3]))
=======
print(sum(total_calories[0:3]))
>>>>>>> 643b2bbafb19c9e46fe5be73ad59e668578e2aa5
