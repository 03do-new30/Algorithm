import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# 양방향 그래프 인접리스트로 저장
a = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    a[parent].append((child, weight))
    a[child].append((parent, weight))

# bfs
def bfs(start):
    q = deque()
    visited = [False] * (n+1)
    dist = [0] * (n+1) #dist[i] = start - i까지의 거리
    q.append(start)
    visited[start] = True

    while q:
        current = q.popleft()
        for next, weight in a[current]:
            if not visited[next]:
                dist[next] = dist[current] + weight
                visited[next] = True
                q.append(next)
    return dist

# 루트에서 가장 먼 노드 x를 구한다
x = 0
tmp = 0
dist_from_root = bfs(1)
for i in range(1, n+1):
    if dist_from_root[i] > tmp:
        tmp = dist_from_root[i]
        x = i
# x에서 가장 먼 노드까지의 거리를 구한다 -> 트리의 지름
max_dist = 0
dist_from_x = bfs(x)
for i in range(1, n+1):
    max_dist = max(max_dist, dist_from_x[i])

print(max_dist)