import sys
input = sys.stdin.readline

n = int(input())

# dp[i][0] = 마지막 수가 0인 i자리 이친수의 개수
# dp[i][0] = dp[i-1][0] + dp[i-1][1]

# dp[i][1] = 마지막 수가 1인 i자리 이친수의 개수
# dp[i][1] = dp[i-1][0]

dp = [[0] * 2 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i][1] = 1
        continue
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))