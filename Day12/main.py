#!/usr/bin/python3

f = open("input.txt")
A = f.read().split("\n")


def solve(A):
    ans = 0
    for line in A:
        s = line.split(" ")[0]
        vals = [int(i) for i in line.split(" ")[1].split(",")]
        n, m = len(s), len(vals)
        dp = [[[0 for _ in range(2)] for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            # Handle operational
            if s[i - 1] == "." or s[i - 1] == "?":
                for j in range(0, m + 1):
                    dp[i][j][0] += dp[i - 1][j][0] + dp[i - 1][j][1]

            # Handle broken
            for j in range(1, m + 1):
                segment = line[max(0, i - vals[j - 1]) : i]
                can = not any(c == "." for c in segment)
                if can and i - vals[j - 1] >= 0:
                    dp[i][j][1] += dp[i - vals[j - 1]][j - 1][0]

        ans += sum(dp[n][m])
    return ans


# Part 1
print(solve(A))

# Part 2
for i, line in enumerate(A):
    s, vals = line.split(" ")
    A[i] = "?".join([s for _ in range(5)]) + " " + ",".join([vals for _ in range(5)])

print(solve(A))
