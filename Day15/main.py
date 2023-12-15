#!/usr/bin/python3

f = open("input.txt")
A = f.read().split(",")


def compute(str):
    c = 0
    for i in str:
        c = ((c + ord(i)) * 17) % 256
    return c


# Part 1
ans = sum(compute(i) for i in A)
print(ans)


# Part 2
buckets = [[] for i in range(256)]
for x in A:
    if "=" in x:
        k, v = x.split("=")
        h = compute(k)
        keys = [i[0] for i in buckets[h]]
        if k in keys:
            buckets[h][keys.index(k)] = (k, v)
        else:
            buckets[h].append((k, v))
    if "-" in x:
        k, v = x.split("-")
        h = compute(k)
        keys = [i[0] for i in buckets[h]]
        if k in keys:
            del buckets[h][keys.index(k)]

ans = 0
for i in range(256):
    for j, p in enumerate(buckets[i]):
        ans += (i + 1) * (j + 1) * int(p[1])
print(ans)
