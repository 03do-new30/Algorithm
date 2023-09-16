import sys
input = sys.stdin.readline

n = int(input())

# dp[i] = i자리 이친수의 개수
# 길이가 i인 이친수, 마지막 숫자가 0인 경우 = dp[i-1]
# 길이가 i인 이친수, 마지막 숫자가 1인 경우 = dp[i-2]
# dp[i] = dp[i-1] + dp[i-2]

dp = [0] * (n+1)
for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n])