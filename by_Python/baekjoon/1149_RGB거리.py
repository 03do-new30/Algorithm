import sys
input = sys.stdin.readline

"""input"""
n = int(input().strip())
cost = [[-1, -1, -1]]
for _ in range(n):
    cost.append(list(map(int, input().split())))
"""input"""

# 첫 번째 집이 각각 R, G, B일 경우에서 시작
# 이전의 집과 겹치지 않는 색들의 최소값을 더해서 비용을 구해감
for i in range(2, n+1):
    # Red
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    # Green
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    # Blue
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[n]))
