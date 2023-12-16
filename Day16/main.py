#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n")
N, M = len(A), len(A[0])
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # ^ < v >


def inside(p):
    return 0 <= p[0] < N and 0 <= p[1] < M


def getOutgoing(i, j, d):
    ans = []
    if A[i][j] == ".":
        ans.append(((i + dir[d][0], j + dir[d][1]), d))

    if A[i][j] == "-" or A[i][j] == "|":
        if bool(d % 2 == 0) ^ bool(A[i][j] == "|"):
            ans.append(
                ((i + dir[(d + 1) % 4][0], j + dir[(d + 1) % 4][1]), (d + 1) % 4)
            )
            ans.append(
                ((i + dir[(d + 3) % 4][0], j + dir[(d + 3) % 4][1]), (d + 3) % 4)
            )
        else:
            ans.append(((i + dir[d][0], j + dir[d][1]), d))

    if A[i][j] == "/" or A[i][j] == "\\":
        if bool(d % 2 == 0) ^ bool(A[i][j] == "/"):
            ans.append(
                ((i + dir[(d + 1) % 4][0], j + dir[(d + 1) % 4][1]), (d + 1) % 4)
            )
        else:
            ans.append(
                ((i + dir[(d + 3) % 4][0], j + dir[(d + 3) % 4][1]), (d + 3) % 4)
            )

    return [i for i in ans if inside(i[0])]


def compute(i, j, d):
    ans = set()
    vis = set()
    q = [((i, j), d)]
    while q:
        v = q.pop()
        if v in vis:
            continue
        vis.add(v)
        (i, j), d = v
        ans.add((i, j))
        for p in getOutgoing(i, j, d):
            q.append(p)
    return len(ans)


# Part 1
print(compute(0, 0, 3))


# Part 2
print(max(compute(0, j, d) for j in range(M) for d in range(3)))
