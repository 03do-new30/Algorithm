import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [[0]]
for _ in range(n):
    dp.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, i+1):
        if i == 1:
            continue
        else:
            if j == i:
                dp[i][j] += dp[i-1][j-1]
            elif j == 1:
                dp[i][j] += dp[i-1][1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(map(max, dp)))
