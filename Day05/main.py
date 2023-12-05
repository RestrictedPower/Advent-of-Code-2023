#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n\n")
init = [int(i) for i in A[0].split("seeds: ")[1].split(" ")]
A = A[1:]


# Part 1
def calc(v):
    vals = [v]
    for line in A:
        newVals = []
        x = line.split("\n")[1:]
        for ln in x:
            d, s, l = [int(it) for it in ln.split(" ")]
            for val in vals:
                if s <= val < s + l:
                    newVals.append(val + d - s)
        if len(newVals) > 0:
            vals = newVals
    return min(vals)


print(min(calc(i) for i in init))

# Part 2
pairs = [[init[i], init[i] + init[i + 1] - 1] for i in range(0, len(init), 2)]

def isStarting(val):
    return any(p[0] <= val <= p[1] for p in pairs)


def reverseCalc(v):
    vals = [v]
    for line in reversed(A):
        newVals = []
        x = line.split("\n")[1:]
        for ln in x:
            d, s, l = [int(it) for it in ln.split(" ")]
            for val in vals:
                if d <= val < d + l:
                    newVals.append(val - (d - s))
        if len(newVals) > 0:
            vals = newVals
    return any(isStarting(i) for i in vals)


step, mx, findOne = 1000, max(p[1] for p in pairs), 1
while 1:
    if reverseCalc(findOne):
        break
    if findOne >= mx:
        break
    findOne += step

for test in range(max(0, findOne - 10 * step), findOne + 1):
    if reverseCalc(test):
        ans = test
        break

print(ans)
