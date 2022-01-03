import sys
input = sys.stdin.readline

n = int(input().strip())
p = [0] + list(map(int, input().split()))

# dp[N] = 카드를 N개 살 때 지불해야하는 금액의 최대값
# dp[N] = max(dp[N-1] + p[1], ..., dp[1] + p[N-1], dp[0] + ][N])
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1:
        dp[1] = p[1]
        continue
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + p[j])
print(dp[n])
