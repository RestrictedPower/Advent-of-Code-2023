#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n")


# Part 1
ans = 0
for line in A:
    x = line.split(": ")[1]
    s = set(i for i in x.split(" | ")[0].split(" ") if len(i) > 0)
    cnt = sum(1 for i in x.split(" | ")[1].split(" ") if i in s)
    if cnt > 0:
        ans += 1 << (cnt - 1)
print(ans)


# Part 2
copies = {}
for i in range(len(A)):
    copies[i + 1] = 1
for idx, line in enumerate(A):
    x = line.split(": ")[1]
    s = set(i for i in x.split(" | ")[0].split(" ") if len(i) > 0)
    cnt = sum(1 for i in x.split(" | ")[1].split(" ") if i in s)
    for i in range(idx + 2, idx + 2 + cnt):
        copies[i] += copies[idx + 1]

print(sum(copies.values()))
