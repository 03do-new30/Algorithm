import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

# 인접리스트
a = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    a[i].append(j)
    a[j].append(i)

# 정점 번호가 작은 것을 먼저 방문할 수 있도록 정렬
for i in range(1, n+1):
    a[i] = sorted(a[i])


# dfs
visited = [False] * (n+1)
def dfs(v):
    visited[v] = True
    print(v, end= ' ')

    for i in range(len(a[v])):
        next = a[v][i]
        if not visited[next]:
            dfs(next)

# bfs
def bfs(v):
    q = deque()
    visited = [False] * (n+1)
    
    q.append(v)
    visited[v] = True

    history = []

    while q:
        v = q.popleft()
        history.append(v)
        for i in range(len(a[v])):
            next = a[v][i]
            if not visited[next]:
                visited[next] = True
                q.append(next)
    
    print(' '.join(list(map(str, history))))
dfs(v)
print()
bfs(v)