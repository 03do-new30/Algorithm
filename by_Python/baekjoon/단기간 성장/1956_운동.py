import sys
input = sys.stdin.readline

v, e = map(int, input().split())
INF = float('inf')
dist = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = c

# 플로이드 워셜로 각 지점에서 다른 지점까지의 최단거리를 구한다.

# 중간 지점을 기준으로
for mid in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])

# dist[node][node]: node에서 출발해서 node에 도착하는 최단거리
ans = INF
for i in range(1, v+1):
    ans = min(ans, dist[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)