#!/usr/bin/python3
f = open("input.txt")
inp = f.read().split("\n\n")
A, B = [i.split("\n") for i in inp]

workflows = {}
values = []

for line in A:
    name, p2 = line.split("{")
    workflows[name] = [rule for rule in p2[:-1].split(",")]


for line in B:
    w = {}
    for p in line[1:-1].split(","):
        a, b = p.split("=")
        w[a] = int(b)
    values.append(w)


def mergeRange(range, newRange):
    l, r = max(range[0], newRange[0]), min(range[1], newRange[1])
    if l <= r:
        return (l, r)
    return None


def update(ranges, indexToUpdate, newRange):
    res = ()
    for i, range in enumerate(ranges):
        if i == indexToUpdate:
            res += (newRange,)
        else:
            res += (range,)
    return res


def solve(ranges):
    q = [("in", ranges)]
    ans = 0
    while q:
        workflow, ranges = q.pop()
        if workflow in ["A", "R"]:
            if workflow == "A":
                pr = 1
                for p in ranges:
                    pr *= p[1] - p[0] + 1
                ans += pr
            continue
        for rule in workflows[workflow]:
            if ":" not in rule:
                q.append((rule, ranges))
                break

            p, jump = rule.split(":")
            letter, op, val = p[0], p[1], int(p[2:])
            idx = ["x", "m", "a", "s"].index(letter)
            segments = {
                "<": ((1, val - 1), (val, 4000)),
                ">": ((val + 1, 4000), (1, val)),
            }

            newRange = mergeRange(ranges[idx], segments[op][0])
            if newRange != None:
                q.append((jump, update(ranges, idx, newRange)))

            newRange = mergeRange(ranges[idx], segments[op][1])
            if newRange == None:
                break
            ranges = update(ranges, idx, newRange)

    return ans


# Part 1
ans = 0
for value in values:
    ranges = ()
    for c in ["x", "m", "a", "s"]:
        ranges += ((value[c], value[c]),)
    if solve(ranges) == 1:
        ans += sum(value.values())
print(ans)

# Part 2
print(solve(((1, 4000), (1, 4000), (1, 4000), (1, 4000))))
