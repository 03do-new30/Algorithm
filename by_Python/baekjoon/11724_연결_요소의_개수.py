import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
# 인접리스트
a = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

visited = [False] * (n+1)

def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = True

    while q:
        u = q.popleft()
        for i in range(len(a[u])):
            v = a[u][i]
            if not visited[v]:
                visited[v] = True
                q.append(v)

# bfs로 탐색을 몇번 하는지 카운트
count = 0
for start in range(1, n+1):
    if not visited[start]:
        bfs(start)
        count += 1

print(count)