import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    visited = [False]*(N+1)
    q = deque([x])
    visited[x] = True
    cnt = 0

    while q:
        x = q.popleft()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
                cnt += 1
    return cnt



N, M = map(int, input().split())
# A가 B를 신뢰한다 -> A는 B의 자손이다.
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

hacking = [0]*(N+1)

for i in range(1, N+1):
    hacking[i] = bfs(i)

# 오름차순 출력
max_hacking = max(hacking)
for i in range(1, N+1):
    if hacking[i] == max_hacking:
        print(i, end= ' ')
print()