#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n\n")
init = [int(i) for i in A[0].split("seeds: ")[1].split(" ")]
A = A[1:]

# Part 2
values = [[init[i], init[i] + init[i + 1] - 1] for i in range(0, len(init), 2)]
for line in A:
    newValues = []
    maps = line.split("\n")[1:]
    added = set()
    while values:
        l, r = values.pop()
        matched = False
        for map in maps:
            dest, source, size = [int(i) for i in map.split()]
            mL, mR, shift = source, source + size - 1, dest - source
            iL, iR = max(l, mL), min(r, mR)
            if iL <= iR:
                matched = True
                newValues.append([iL + shift, iR + shift])
                cL = max(l, mR + 1)
                if cL <= r:
                    values.append([cL, r])
                cR = min(r, mL - 1)
                if l <= cR:
                    values.append([l, cR])
                break
        if not matched:
            newValues.append([l, r])
    values = newValues

print(min(i[0] for i in values))
