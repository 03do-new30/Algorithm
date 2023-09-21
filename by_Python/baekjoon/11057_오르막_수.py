import sys
input = sys.stdin.readline

n = int(input().strip())
mod = 10007

#dp[i][j] = i번째 자리에 수j가 올 때, 가능한 경우의 수
dp = [[0] * 10 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(10):
        if i == 1:
            dp[i][j] = 1
        elif j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % mod

print(sum(dp[n]) % mod)
