import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())

dist = [[INF] * (n+1) for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c) # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있음

# 자기 자신의 비용 0으로 설정
for i in range(1, n+1):
    dist[i][i] = 0

# Floyd Warshall - 중간 지점을 기준으로!
for mid in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j]= min(dist[i][j], dist[i][mid] + dist[mid][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()