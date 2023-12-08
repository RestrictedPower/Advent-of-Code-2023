#!/usr/bin/python3
import math

f = open("input.txt")
x = f.read().split("\n")

instr = x[0]
x = x[2:]

mp = {}
for line in x:
    s = line.split(" = ")[0]
    x = line.split(" = ")[1].split(", ")
    l = x[0][1:]
    r = x[1][:-1]
    mp[s] = (l, r)

# Part 1
cur = "AAA"
idx = 0
while cur != "ZZZ":
    cur = mp[cur][{"L": 0, "R": 1}[instr[idx % len(instr)]]]
    idx += 1
print(idx)


# Part 2
all = [i for i in mp.keys() if i[-1] == "A"]
ans = 1
for cur in all:
    idx = 0
    while cur[-1] != "Z":
        cur = mp[cur][{"L": 0, "R": 1}[instr[idx % len(instr)]]]
        idx += 1
    ans = math.lcm(ans, idx)
print(ans)


