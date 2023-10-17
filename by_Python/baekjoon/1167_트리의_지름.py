import sys
input = sys.stdin.readline
from collections import deque

v = int(input())
a = [[] for _ in range(v+1)]
for _ in range(v):
    infos = list(map(int, input().split()))
    n = infos[0]
    idx = 1
    while infos[idx] != -1:
        u = infos[idx]
        dist = infos[idx + 1]
        a[n].append((u, dist))
        idx += 2

# BFS를 이용하여 트리의 지름 구하기
def bfs(start):
    q = deque()
    q.append(start)
    visited = [False] * (v + 1)
    visited[start] = True
    dist = [0] * (v + 1) # dist[i] = start에서 i까지의 거리 저장

    while q:
        node = q.popleft()
        for next, next_dist in a[node]:
            if not visited[next]:
                visited[next] = True
                dist[next] = dist[node] + next_dist
                q.append(next)
    return dist

# 임의의 정점, 문제에서 항상 존재하는 1에서 가장 먼 정점 x를 찾는다
dist_from_1 = bfs(1)
max_dist = 0
x= 0
for i in range(1, v+1):
    if max_dist < dist_from_1[i]:
        max_dist = dist_from_1[i]
        x = i

# x에서 가장 먼 정점까지의 거리를 찾는다
final_dist = bfs(x)
max_dist = 0
for i in range(1, v+1):
    if max_dist < final_dist[i]:
        max_dist = final_dist[i]

print(max_dist)