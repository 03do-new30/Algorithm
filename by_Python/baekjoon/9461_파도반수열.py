import sys
input = sys.stdin.readline

p = [0 for _ in range(101)]
p[1] = p[2] = p[3] = 1
p[4] = 2

# p[i] = p[i-1] + p[i-5]


def dp(n):
    if n < 5:
        return p[n]
    if p[n] != 0:
        return p[n]
    p[n] = dp(n-1) + dp(n-5)
    return p[n]


for _ in range(int(input().strip())):
    n = int(input().strip())
    print(dp(n))
