import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, visited):
    q = deque([])
    q.append(start)
    visited[start] = 0 # 시작은 0번 그룹
    # 0번 그룹에서 나가서 도착하는 정점은 1번 그룹으로 만듦

    while q:
        start = q.popleft()
        for i in range(len(a[start])):
            next = a[start][i]
            if visited[next] == -1: #미방문
                if visited[start] == 0:
                    visited[next] = 1
                else:
                    visited[next] = 0
                q.append(next)
            else: # 방문한 그래프
                if visited[start] == visited[next]:
                    return False
    return True


k = int(input())
for _ in range(k):
    n, e = map(int, input().split())
    # 인접리스트
    a = [[] for x in range(n+1)]
    for __ in range(e):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)
    
    visited = [-1] * (n+1)

    for start in range(1, n+1):
        if visited[start] == -1:
            bipartite = bfs(start, visited)
            if not bipartite:
                break
    
    if bipartite:
        print("YES")
    else:
        print("NO")