#!/usr/bin/python3

f = open("input.txt")
x = f.read().split("\n")


# Part 1
cap = {"red": 12, "green": 13, "blue": 14}
ans = 0
for line in x:
    good = True
    for part in line.split(": ")[1].split("; "):
        for col in part.split(", "):
            col = col.split(" ")
            good &= cap[col[1]] >= int(col[0])
    if good:
        ans += int(line.split(": ")[0].split("Game ")[1])
print(ans)


# Part 2
ans = 0
for line in x:
    good = True
    mn = {"red": 0, "green": 0, "blue": 0}
    for part in line.split(": ")[1].split("; "):
        for col in part.split(", "):
            col = col.split(" ")
            mn[col[1]] = max(mn[col[1]], int(col[0]))
    ans += mn["red"] * mn["green"] * mn["blue"]
print(ans)
