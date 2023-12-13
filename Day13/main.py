#!/usr/bin/python3

f = open("input.txt")
AA = f.read().split("\n\n")


def col(A, j):
    return "".join([A[i][j] for i in range(len(A))])


# Part 1
ans = 0
for A in AA:
    A = A.split("\n")
    N, M = len(A), len(A[0])

    for j in range(0, M - 1):
        x = min(M - j - 1, j + 1)
        if all(col(A, j - i) == col(A, j + 1 + i) for i in range(x)):
            ans += j + 1

    for i in range(0, N - 1):
        x = min(N - i - 1, i + 1)
        if all(A[i - j] == A[i + 1 + j] for j in range(x)):
            ans += (i + 1) * 100
print(ans)


# Part 2
def diffCnt(A, B):
    return sum([1 for i in range(len(A)) if A[i] != B[i]])


ans = 0
for A in AA:
    A = A.split("\n")
    N, M = len(A), len(A[0])

    for j in range(0, M - 1):
        x = min(M - j - 1, j + 1)
        if sum(diffCnt(col(A, j - i), col(A, j + 1 + i)) for i in range(x)) == 1:
            ans += j + 1

    for i in range(0, N - 1):
        x = min(N - i - 1, i + 1)
        if sum(diffCnt(A[i - j], A[i + 1 + j]) for j in range(x)) == 1:
            ans += (i + 1) * 100
print(ans)
