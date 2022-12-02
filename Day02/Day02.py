"""
Created on Fri Dec  2 21:28:22 2022

@author: tricialyjun
"""

with open("strategyguide", "r") as f:
    strat_guide = f.read().strip().split("\n")

strat_key = {'A': 0, 'B': 1, 'C': 2, 
              'X': 0, 'Y': 1, 'Z': 2}

trans_guide = [[strat_key.get(ii[0], ii[0]), strat_key.get(ii[-1], ii[-1])] for ii in strat_guide]

# Part 1
outcome1 = [ii[1]+1 + ((ii[1]-ii[0])%3+1)%3*3 for ii in trans_guide]
print(sum(outcome1))

# Part 2
outcome2 = [(ii[0]+ii[1]+2)%3+1 + ii[1]*3 for ii in trans_guide]
print(sum(outcome2))