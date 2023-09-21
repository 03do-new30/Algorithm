import sys
input = sys.stdin.readline

n = int(input().strip())

# dp[i][0] = i번째 행에 사자를 배치하지 않는 경우의수 = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
# dp[i][1] = i번째 행 첫번째 칸에 사자를 배치하는 경우의 수 = dp[i-1][0] + dp[i-1][2] = dp[i][0] - dp[i-1][1]
# dp[i][2] = i번째 행 두번째 칸에 사자를 배치하는 경우의 수 = dp[i-1][0] + dp[i-1][1] = dp[i][0] - dp[i-1][2]
dp = [[0] * 3 for _ in range(n+1)]
dp[0][0] = 1

mod = 9901

for i in range(1, n+1):
    dp[i][0] = sum(dp[i-1]) % mod
    dp[i][1] = (dp[i][0] - dp[i-1][1]) % mod
    dp[i][2] = (dp[i][0] - dp[i-1][2]) % mod

print(sum(dp[n]) % mod)
