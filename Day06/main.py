#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n")

def can(val, t, d):
    return (t - val) * val > d

# Part 1
t = [int(i) for i in A[0].split(":")[1].split(" ") if len(i) > 0]
d = [int(i) for i in A[1].split(":")[1].split(" ") if len(i) > 0]
ans = 1
for idx, time in enumerate(t):
    cnt = 0
    for i in range(time):
        if can(i, time, d[idx]):
            cnt += 1
    ans *= cnt
print(ans)


# Part 2
t = int("".join([i for i in A[0].split(":")[1].split(" ") if len(i) > 0]))
d = int("".join([i for i in A[1].split(":")[1].split(" ") if len(i) > 0]))

mid, l, r = t // 2, 0, 0
for i in reversed(range(30)):
    if can(mid - (l + (1 << i)), t, d):
        l += 1 << i
    if can(mid + (r + (1 << i)), t, d):
        r += 1 << i

ans = l + r + {True: 1, False: 0}[can(mid, t, d)]
print(ans)
