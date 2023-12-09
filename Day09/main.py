#!/usr/bin/python3
import math

f = open("input.txt")
x = f.read().split("\n")

# Part 1
ans = 0
for line in x:
    line = [int(i) for i in line.split(" ")]
    lines = [line]
    prev = line
    while True:
        next = [prev[i + 1] - prev[i] for i in range(len(prev) - 1)]
        lines.append(next)
        if all(False for i in next if i != 0):
            break
        prev = next
    lst, i = 0, len(lines) - 1
    while i >= 0:
        lst = lines[i][-1] + lst
        i -= 1
    ans += lst
print(ans)

# Part 2
ans = 0
for line in x:
    line = [int(i) for i in line.split(" ")]
    lines = [line]
    prev = line
    while True:
        next = [prev[i + 1] - prev[i] for i in range(len(prev) - 1)]
        lines.append(next)
        if all(False for i in next if i != 0):
            break
        prev = next
    lst, i = 0, len(lines) - 1
    while i >= 0:
        lst = lines[i][0] - lst
        i -= 1
    ans += lst
print(ans)
