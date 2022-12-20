"""
Created on Tue Dec 20 00:11:02 2022

@author: tricialyjun
"""

with open("signal", "r") as f:
    signal = f.read()

# Part 1
counter = 4
readframe = signal[:counter]
while len(set(readframe)) < 4:
    counter += 1
    readframe = signal[counter-4:counter]
    
print(counter)

# Part 2
counter2 = 14
readframe = signal[:counter2]
while len(set(readframe)) < 14:
    counter2 += 1
    readframe = signal[counter2-14:counter2]
    
print(counter2)

