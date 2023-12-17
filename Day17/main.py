#!/usr/bin/python3
from queue import PriorityQueue

f = open("input.txt")
A = f.read().split("\n")
N, M = len(A), len(A[0])
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def inside(p):
    return 0 <= p[0] < N and 0 <= p[1] < M


def solve(minstep, maxStep):
    pq = PriorityQueue()
    pq.put((0, (0, 0, 0)))
    pq.put((0, (0, 0, 1)))
    mp = {}
    while not pq.empty():
        cur = pq.get()
        cost, state = cur
        if state in mp:
            continue
        mp[state] = cost
        i, j, d = state
        for nD in range(4):
            if (d + nD) % 2 == 0:
                continue
            c = 0
            for moves in range(1, maxStep + 1):
                nI, nJ = i + dir[nD][0] * moves, j + dir[nD][1] * moves
                if not inside((nI, nJ)):
                    break
                c += int(A[nI][nJ])
                if moves >= minstep:
                    pq.put((cost + c, (nI, nJ, nD)))

    return min(mp[i] for i in mp if i[0] == N - 1 and i[1] == M - 1)


# Part 1
print(solve(1, 3))

# Part 2
print(solve(4, 10))
