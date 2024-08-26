import sys
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 최단거리 테이블
dist = [INF] * (n+1)

def bellman_ford(start):
    dist[start] = 0
    # (n-1)번 모든 간선 검사를 반복한다. 나머지 한번은 음의 사이클을 감지하는 데 쓴다.
    for i in range(n):
        # print("dist:", dist)
        for current, next, weight in edges:
            if dist[current] == INF:
                continue
            if dist[next] > dist[current] + weight:
                # n번째 반복에 갱신되는 최단거리가 있다면 음의 사이클 존재
                if i == n-1:
                    return False 
                dist[next] = dist[current] + weight
    return True

if bellman_ford(1):
    for city in range(2, n+1):
        print(dist[city] if dist[city] != INF else -1)
else:
    print(-1)