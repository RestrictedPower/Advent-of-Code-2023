f = open("input.txt")
x = f.read().split()

mp = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# Part 1
def part1(x):
    l = r = "-"
    for idx in range(len(x)):
        c = x[idx]
        if not c.isdigit():
            continue
        val = ord(c) - ord("0")
        if l == "-":
            l = val
        r = val
    return l * 10 + r


res = sum([part1(i) for i in x])
print(res)


# Part 2
def part2(x):
    l = r = "-"
    for idx in range(len(x)):
        c = x[idx]
        val = "-"
        for i in mp:
            v = x[idx : (idx + len(i))]
            if v == i:
                val = mp[i]
        if c.isdigit():
            val = ord(c) - ord("0")
        if val == "-":
            continue
        if l == "-":
            l = val
        r = val
    return l * 10 + r


res = sum([part2(i) for i in x])
print(res)
