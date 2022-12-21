"""
Created on Wed Dec 21 22:23:24 2022

@author: tricialyjun
"""
monkeys = {}
lowestcommon = 1
with open("keepaway", "r") as f:
    for line in f:
        line = line.replace(":","").strip()
        if line.startswith("Monkey"):
            key = line.split(" ")[-1]
            monkeys[key] = {}
            monkeys[key]["counter"] = 0
        elif line.startswith("Starting"):
            itemlist = line.replace("Starting items ","").split(", ")
            monkeys[key]["items"] = [int(_) for _ in itemlist]
        elif line.startswith("Operation"):
            monkeys[key]["operation"] = line.replace("Operation new = ","")
        elif line.startswith("Test"):
            mod = line.replace("Test divisible by ","")
            lowestcommon *= int(mod)
        elif line.startswith("If true"):
            trueval = line[-1]
        elif line.startswith("If false"):
            falseval = line[-1]
            monkeys[key]["throw"] = "lambda x: " + trueval + " if x%" + mod + " == 0 else " + falseval

# Part 1
for rr in range(20):
    for mm in range(8):
        for old in monkeys[str(mm)]["items"]:
            new = int(eval(monkeys[str(mm)]["operation"])/3)
            throwto = eval(monkeys[str(mm)]["throw"])(new)
            monkeys[str(throwto)]["items"].append(new)
            monkeys[str(mm)]["counter"] += 1
        monkeys[str(mm)]["items"] = []

activity = [value['counter'] for value in monkeys.values()]
mb1 = activity.pop(activity.index(max(activity)))
mb2 = max(activity)
print(mb1*mb2)

# Part 2
### Reset monkeys from file
for rr in range(10000):
    for mm in range(8):
        for old in monkeys[str(mm)]["items"]:
            new = eval(monkeys[str(mm)]["operation"])%lowestcommon
            throwto = eval(monkeys[str(mm)]["throw"])(new)
            monkeys[str(throwto)]["items"].append(new)
            monkeys[str(mm)]["counter"] += 1
        monkeys[str(mm)]["items"] = []
        
activity2 = [value['counter'] for value in monkeys.values()]
mb1 = activity2.pop(activity2.index(max(activity2)))
mb2 = max(activity2)
print(mb1*mb2)