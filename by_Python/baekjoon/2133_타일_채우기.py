import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    if i % 2 != 0:
        continue

    dp[i] += dp[i-2] * 3

    for j in range(4, i+1, 2):
        if i - j < 0:
            break
        dp[i] += dp[i-j] * 2

print(dp[n])