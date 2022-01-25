import sys
from collections import deque
sys.setrecursionlimit(10**9)  # for dfs
input = sys.stdin.readline

n = int(input().strip())

# 노드의 개수가 1000,000개까지 주어질 수 있으므로
# 인접 행렬이 아닌 인접 리스트로 구현한다
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# bfs


def bfs(start, visited, parent):
    q = deque([])
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = True
                parent[w] = v

# dfs


def dfs(start, visited, parent):
    for v in graph[start]:
        if not visited[v]:
            visited[v] = True
            parent[v] = start
            dfs(v, visited, parent)


parent = [0]*(n+1)
visited = [False]*(n+1)
bfs(1, visited, parent)
#dfs(1, visited, parent)
for i in range(2, n+1):
    print(parent[i])
