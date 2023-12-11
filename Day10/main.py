#!/usr/bin/python3

f = open("input.txt")
x = f.read().split("\n")
N, M = len(x), len(x[0])

north = (-1, 0)
south = (1, 0)
west = (0, -1)
east = (0, 1)

v = {
    "|": [north, south],
    "-": [east, west],
    "L": [north, east],
    "J": [north, west],
    "7": [south, west],
    "F": [south, east],
    "S": [north, south, west, east],
}


def inside(i, j):
    return 0 <= i < N and 0 <= j < M


def outgoing(i, j):
    if not inside(i, j) or x[i][j] not in v:
        return []
    return [(e[0] + i, e[1] + j) for e in v[x[i][j]] if inside(e[0] + i, e[1] + j)]


def getConnections(i, j):
    return [(e[0], e[1]) for e in outgoing(i, j) if (i, j) in outgoing(e[0], e[1])]


def distMap(x):
    pos = [(i, j) for i in range(N) for j in range(M) if x[i][j] == "S"][0]
    mp = {pos: 0}
    q = [pos]
    ans = 0
    while q:
        cur = q.pop(0)
        ans = max(ans, mp[cur])
        for to in getConnections(cur[0], cur[1]):
            if to in mp:
                continue
            mp[to] = mp[cur] + 1
            q.append(to)
    return mp


# Part 1
loop = distMap(x)
print(max(loop.values()))


# Part 2
expandMap = {
    "|": [".|.", ".|.", ".|."],
    "-": ["...", "---", "..."],
    "L": [".|.", ".L-", "..."],
    "J": [".|.", "-J.", "..."],
    "7": ["...", "-7.", ".|."],
    "F": ["...", ".F-", ".|."],
    ".": ["...", "...", "..."],
    "S": [".|.", "-S-", ".|."],
}


def expand(x):
    res = ["" for _ in range(len(x) * 3)]
    for i in range(len(x)):
        for j in range(len(x[0])):
            a = expandMap[x[i][j]]
            res[i * 3] += a[0]
            res[i * 3 + 1] += a[1]
            res[i * 3 + 2] += a[2]
    return res


x = expand(x)
N, M = len(x), len(x[0])
dm = distMap(x)

outside = 0
q = [(0, 0)]
vis = set(q[0])
while q:
    i, j = q.pop()
    if i % 3 == 1 and j % 3 == 1:
        outside += 1
    for i, j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if inside(i, j) and (i, j) not in vis and (i, j) not in dm:
            vis.add((i, j))
            q.append((i, j))

ans = (N * M // 9) - len(loop) - outside
print(ans)
