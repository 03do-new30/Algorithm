import sys
input = sys.stdin.readline

n = int(input().strip())
s = list(map(int, input().split()))
dp = [-2000 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[0] = s[0]
        continue

    dp[i] = max(dp[i-1] + s[i], s[i])

print(max(dp))
