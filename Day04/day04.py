#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:44:56 2022

@author: tricialyjun
"""

with open("sections", "r") as f:
    sections = f.read().strip().replace("-", ",").split("\n")
sections = [[int(y) for y in x.split(",")] for x in sections]
set_1    = [set(range(x[0],x[1]+1)) for x in sections]
set_2    = [set(range(x[2],x[3]+1)) for x in sections]

# Part 1
count_subsets = 0
for ii in range(len(sections)):
    if set_1[ii].issuperset(set_2[ii]) or set_1[ii].issubset(set_2[ii]):
        count_subsets += 1
print(count_subsets)

# Part 2
count_intersects = 0
for ii in range(len(sections)):
    if not set_1[ii].isdisjoint(set_2[ii]):
        count_intersects += 1
print(count_intersects)