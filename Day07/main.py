#!/usr/bin/python3
import functools
from functools import lru_cache

f = open("input.txt")
A = f.read().split("\n")


def strength(val):
    return len(chars) - chars.index(val)


def type(item):
    f = {}
    for c in item:
        if not c in f:
            f[c] = 0
        f[c] += 1
    mx = max(f.values())
    if mx > 3:
        return mx + 1
    if mx == 1:
        return 0
    second = sorted(f.values())[-2]
    if mx == 3:
        if second == 2:
            return 4
        return 3
    # mx = 2
    if second == 2:
        return 2
    return 1


# Part 1
chars = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def compare(item1, item2):
    item1 = item1.split(" ")[0]
    item2 = item2.split(" ")[0]
    t1, t2 = type(item1), type(item2)
    if t1 == t2:
        for i in range(len(item1)):
            cmp = strength(item1[i]) - strength(item2[i])
            if cmp != 0:
                return cmp
    return t1 - t2


A = sorted(A, key=functools.cmp_to_key(compare))
ans = 0
for i, v in enumerate(A):
    ans += (i + 1) * int(v.split(" ")[1])
print(ans)


# Part 2
chars = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


@lru_cache(maxsize=None)
def getMax(item):
    return sorted(
        [item.replace("J", c) for c in chars], key=functools.cmp_to_key(compare)
    )[-1]


def compare2(item1, item2):
    item1 = item1.split(" ")[0]
    item2 = item2.split(" ")[0]
    t1, t2 = type(getMax(item1)), type(getMax(item2))
    if t1 == t2:
        for i in range(len(item1)):
            cmp = strength(item1[i]) - strength(item2[i])
            if cmp != 0:
                return cmp
    return t1 - t2


A = sorted(A, key=functools.cmp_to_key(compare2))
ans = 0
for i, v in enumerate(A):
    ans += (i + 1) * int(v.split(" ")[1])
print(ans)
