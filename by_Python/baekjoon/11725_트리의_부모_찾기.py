import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# 인접리스트로 만듦
a = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

# 루트부터 탐색하면서 각 노드의 부모를 구한다
parent = [-1] * (n+1)
def bfs(start):
    q = deque()
    q.append(start)
    visited = [False] * (n+1)
    visited[start] = True

    while q:
        u = q.popleft()
        for v in a[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                q.append(v)

bfs(1)

for i in range(2, n+1):
    print(parent[i])