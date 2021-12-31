import sys
input = sys.stdin.readline

n = int(input().strip())
wine = [int(input().strip()) for _ in range(n)]

# dp[i] = i번째 잔까지 왔을 때, 마실 수 있는 최대 양
dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[0] = wine[0]
        continue
    if i == 1:
        dp[1] = wine[0] + wine[1]
        continue
    dp[i] = max(dp[i-2] + wine[i],
                dp[i-3] + wine[i-1] + wine[i],
                dp[i-1])
print(max(dp))
