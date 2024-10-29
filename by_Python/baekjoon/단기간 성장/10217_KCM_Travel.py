import sys
input = sys.stdin.readline

t = int(input())
# n: 공항 수, m: 총 지원 비용, k: 티켓 정보 수
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(k):
    u, v, c, d = map(int, input().split())
    graph[u].append((v, c, d)) # (도착, 비용, 시간)

# dp[i][j] = i공항에 j원을 써서 도착할 때 걸리는 최소 시간
INF = float('inf')
dp = [[INF] * (m+1) for _ in range(n+1)]
dp[1][0] = 0

for money in range(m+1):
    for airport in range(1, n+1):
        if dp[airport][money] == INF:
            continue
        for next_airport, cost, time in graph[airport]:
            if money + cost > m:
                continue
            dp[next_airport][money + cost] = min(dp[next_airport][money + cost], dp[airport][money] + time)

shortest_time = min(dp[n])
if shortest_time == INF:
    print("Poor KCM")
else:
    print(shortest_time)