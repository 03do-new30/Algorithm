import sys
input = sys.stdin.readline

n = int(input().strip())
wine = [0] + [int(input().strip()) for _ in range(n)]

# dp[i] = i번째 잔까지 왔을 때, 마실 수 있는 최대 양
dp = [0 for _ in range(n+1)]

# dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
for i in range(1, n+1):
    if i == 1:
        dp[i] = wine[i]
        continue
    if i == 2:
        dp[i] = wine[i] + wine[i-1]
        continue

    if i - 1 >= 0:
        dp[i] = dp[i-1]

    if i - 2 >= 0:
        dp[i] = max(dp[i], dp[i-2] + wine[i])

    if i - 3 >= 0:
        dp[i] = max(dp[i], dp[i-3] + wine[i-1] + wine[i])

print(max(dp))