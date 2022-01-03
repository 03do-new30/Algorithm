import sys
input = sys.stdin.readline

t = int(input().strip())


def dp(d, n, m):
    if d[n][m] != 0:
        return d[n][m]

    if n == 1:
        d[n][m] = m
    elif n == m:
        d[n][m] = 1
    else:
        d[n][m] = dp(d, n-1, m-1) + dp(d, n, m-1)
    return d[n][m]


for _ in range(t):
    n, m = map(int, input().split())

    # mCn = (m-1)C(n-1) + (m-1)Cn
    d = [[0] * (m+1) for _ in range(n+1)]
    print(dp(d, n, m))
