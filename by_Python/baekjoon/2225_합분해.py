import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# dp[k][n] = 정수 k개를 더해서 합이 n이 되는 경우의 수
dp = [[0] * (N+1) for _ in range(K+1)]

mod = 1000000000
for k in range(1, K+1):
    for n in range(N+1):
        if k == 1:
            dp[k][n] = 1
            continue
        if n == 0:
            dp[k][n] = 1
            continue
        for i in range(n+1):
            dp[k][n] += dp[k-1][n-i]
            dp[k][n] %= mod

print(dp[K][N])