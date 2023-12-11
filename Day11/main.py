#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n")

N, M = len(A), len(A[0])
x = [j for j in range(M) if all(A[i][j] == "." for i in range(N))]
y = [i for i in range(N) if all(A[i][j] == "." for j in range(M))]
points = [(i, j) for i in range(N) for j in range(M) if A[i][j] == "#"]

# Part 1
ans = 0
for A in points:
    for B in points:
        mnI, mxI = sorted([A[0], B[0]])
        mnJ, mxJ = sorted([A[1], B[1]])
        ans += mxI + mxJ - mnI - mnJ
        ans += sum([1 for i in y if mnI < i < mxI])
        ans += sum([1 for j in x if mnJ < j < mxJ])
ans //= 2
print(ans)

# Part 2
ans = 0
for A in points:
    for B in points:
        mnI, mxI = sorted([A[0], B[0]])
        mnJ, mxJ = sorted([A[1], B[1]])
        ans += mxI + mxJ - mnI - mnJ
        v = int(1e6)
        ans += sum([v - 1 for i in y if mnI < i < mxI])
        ans += sum([v - 1 for j in x if mnJ < j < mxJ])
ans //= 2
print(ans)
