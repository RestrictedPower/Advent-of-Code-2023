#!/usr/bin/python3
f = open("input.txt")
A = f.read().split("\n")
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirL = {"R": 0, "D": 1, "L": 2, "U": 3}

# Find area by using (https://en.wikipedia.org/wiki/Shoelace_formula)
# And then use Pick's theorem (https://en.wikipedia.org/wiki/Pick%27s_theorem)

# Part 1
i, j = 0, 0
prev = (0, 0)
area = 0
boundary = 0
for line in A:
    d, a, rgb = line.split(" ")
    d, a = dirL[d], int(a)
    i += dir[d][0] * a
    j += dir[d][1] * a
    boundary += a
    area += prev[0] * j - prev[1] * i
    prev = (i, j)

area = abs(area) // 2
interior = area - boundary // 2 + 1
print(interior + boundary)


# Part 2
i, j = 0, 0
prev = (0, 0)
area = 0
boundary = 0
for line in A:
    d, a, rgb = line.split(" ")
    a, d = int(rgb[2:-2], 16), int(rgb[-2])
    i += dir[d][0] * a
    j += dir[d][1] * a
    boundary += a
    area += prev[0] * j - prev[1] * i
    prev = (i, j)

area = abs(area) // 2
interior = area - boundary // 2 + 1
print(interior + boundary)
