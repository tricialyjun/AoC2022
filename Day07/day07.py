"""
Created on Tue Dec 20 21:29:57 2022

@author: tricialyjun
"""

with open("terminaloutput", "r") as f:
    outputLog = f.read().strip().split("\n") 

filesystem = {}
pathname = ''
filesystem['/'] = []
for ii in outputLog[1:]:
    if ii == '$ cd ..':
        pathname = '/'.join(pathname.split('/')[:-1])
    elif ii[:4] == '$ cd':
        pathname = pathname + '/' + ii.split(" ")[-1] 
        filesystem[pathname] = []
    elif ii[0].isnumeric():
        filename = pathname + '/' + ii.split(" ")[-1]
        filesystem[filename] = ii.split(" ")[0]
        
folders = [k for k,v in filesystem.items() if v == []]
files   = [k for k,v in filesystem.items() if v != []]

foldersizes = []
for jj in reversed(folders):
    foldersizes.append(sum([int(filesystem[kk]) for kk in files if kk.startswith(jj)]))

# Part 1
print(sum([_ for _ in foldersizes if _ <= 100000]))


# Part 2
spaceunused = 70000000 - max(foldersizes)
spacetofree = 30000000 - spaceunused
min([ll for ll in foldersizes if ll > spacetofree])