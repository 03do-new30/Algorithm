import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

min_cost = 1000000

# 첫번째 집을 칠하는 색(first)을 고정해두고 구해본다
for first in range(3):
    dp = [[0, 0, 0] for _ in range(n)]
    for i in range(n):
        for j in range(3):
            if i == 0 and j != first:
                dp[i][j] = 1000000
                continue
            if i == 0:
                dp[i][j] = cost[i][j]
                continue

            if i == n-1 and j == first:
                dp[i][j] = 1000000
                continue

            if j == 0:
                dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + cost[i][j]
            elif j == 1:
                dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + cost[i][j]
            else:
                dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + cost[i][j]
    min_cost = min(min_cost, min(dp[n-1]))

print(min_cost)