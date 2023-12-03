#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n")


def around(i, j):
    nums = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (0 <= x + i < len(A) and 0 <= y + j < len(A[0])):
                continue
            if not A[x + i][y + j].isdigit() and A[x + i][y + j] != ".":
                nums.append((x + i, y + j))
    return nums


# Part 1
ans = 0
for idx, line in enumerate(A):
    for i in range(len(line)):
        if not line[i].isdigit() or i > 0 and line[i - 1].isdigit():
            continue
        take = len(around(idx, i)) > 0
        j = i
        while j + 1 < len(line) and line[j + 1].isdigit():
            j += 1
            take |= len(around(idx, j)) > 0
        v = int(line[i : j + 1])
        if take:
            ans += v
print(ans)


# Part 2
vals = {}
for idx, line in enumerate(A):
    for i in range(len(line)):
        if not line[i].isdigit() or i > 0 and line[i - 1].isdigit():
            continue
        s = set()
        s.update(around(idx, i))
        j = i
        while j + 1 < len(line) and line[j + 1].isdigit():
            j += 1
            s.update(around(idx, j))
        v = int(line[i : j + 1])
        for i in s:
            if i not in vals:
                vals[i] = []
            vals[i].append(v)
ans = sum(vals[i][0] * vals[i][1] for i in vals if len(vals[i]) == 2)
print(ans)
