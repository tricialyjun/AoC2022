"""
Created on Sat Dec  3 22:52:19 2022

@author: tricialyjun
"""

with open("rucksacks", "r") as f:
    rucksacks = f.read().strip().split("\n")

priority_map  = [chr(x) for x in list(range(ord('a'),ord('z')+1))] + [chr(x) for x in list(range(ord('A'),ord('Z')+1))] 

# Part 1
compartment_1 = [x[:int(len(x)/2)] for x in rucksacks]
compartment_2 = [x[int(len(x)/2):] for x in rucksacks]
common_item = [list(set(c1).intersection(c2)) for c1, c2 in zip (compartment_1, compartment_2)]
common_item = sum(common_item, [])

item_values = [priority_map.index(x)+1 for x in common_item]
print(sum(item_values))

# Part 2
badge = [list(set(e1)&set(e2)&set(e3)) for e1, e2, e3 in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])]
badge = sum(badge, [])
badge_values = [priority_map.index(x)+1 for x in badge]
print(sum(badge_values))