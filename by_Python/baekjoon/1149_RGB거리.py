import sys
input = sys.stdin.readline

"""input"""
n = int(input().strip())
cost = [[-1, -1, -1]]
for _ in range(n):
    cost.append(list(map(int, input().split())))
"""input"""

# dp[i][color] = i번 집이 color 색상으로 집을 칠했을 때, 
#                1 ~ i번 집을 칠하는 데 드는 총 최소 비용
dp = [[0] * 3 for _ in range(n+1)]
for i in range(1, n+1):
    for color in range(n):
        if color == 0:
            dp[i][color] = min(dp[i-1][1], dp[i-1][2]) + cost[i][color]
        elif color == 1:
            dp[i][color] = min(dp[i-1][0], dp[i-1][2]) + cost[i][color]
        elif color == 2:
            dp[i][color] = min(dp[i-1][0], dp[i-1][1]) + cost[i][color]

print(min(dp[n]))