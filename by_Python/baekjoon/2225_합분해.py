import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# dp[k][n] -> k개를 더해서 합이 n
# dp[k][n] = dp[k-1][n] + dp[k][n-1]
dp = [[0]*(N+1) for _ in range(K+1)]
# dp[x][0] = 1로 초기화
# dp[1][X] = 1로 초기화
for i in range(1, K+1):
    dp[i][0] = 1
for i in range(1, N+1):
    dp[1][i] = 1


for k in range(1, K+1):
    for n in range(1, N+1):
        if dp[k][n] == 1:
            continue  # skip
        dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % 1000000000

print(dp[K][N])
