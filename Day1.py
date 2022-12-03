import numpy as np

with open("input.txt", 'r') as f:
    elves = f.read().split("\n\n")

elves = list(map(lambda a : a.split("\n"), elves))
elves[-1].pop()  # Last element of last elf was ''
cals = list(map(lambda a : sum([eval(x) for x in a]), elves))

max = sorted(cals)[-1]
print(max)

max3 = sum(sorted(cals)[-3:])
print(max3)
