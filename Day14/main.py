#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n")
A = [list(i) for i in A]

N, M = len(A), len(A[0])
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]


# This is 100% unoptimal, but at least easy to implement.
def move(A, dir):
    B = [[A[i][j] for j in range(M)] for i in range(M)]
    changed = True
    while changed:
        changed = False
        for i in range(N):
            for j in range(M):
                nI, nJ = dirs[dir % 4][0] + i, dirs[dir % 4][1] + j
                if 0 <= nI < N and 0 <= nJ < M:
                    if B[nI][nJ] == "." and B[i][j] == "O":
                        B[i][j], B[nI][nJ] = B[nI][nJ], B[i][j]
                        changed = True
    return B


# Part 1
B = move(A, 0)
ans = sum([N - i for i in range(N) for j in range(M) if B[i][j] == "O"])
print(ans)


# Part 2
def cycle(A):
    B = A
    for i in range(4):
        B = move(B, i)
    return B


moves, idx = 1000000000, 0
seen = {}
while moves > 0:
    A = cycle(A)
    idx += 1
    moves -= 1
    h = "".join("".join(i) for i in A)
    if h in seen:
        moves %= idx - seen[h]
    else:
        seen[h] = idx

ans = sum([N - i for i in range(N) for j in range(M) if A[i][j] == "O"])
print(ans)
