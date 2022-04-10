import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(1, 0)]) # (번호, depth). depth 2까지만 초대한다.
    visited = [False]*(n+1)
    visited[1] = True

    invite = 0

    while q:
        x, depth = q.popleft()
        if depth <= 1:
            for y in graph[x]:
                if not visited[y]:
                    q.append((y, depth + 1))
                    visited[y] = True
                    invite += 1
    
    return invite

        
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs())