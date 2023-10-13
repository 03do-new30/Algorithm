import sys
input = sys.stdin.readline
from collections import deque

sys.setrecursionlimit(1000000)

n = int(input())
# 인접 리스트
a = [[] for _ in range(n+1)]
for _ in range(n):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

# 방문여부
visited = [0]*(n+1) # 0: 방문X, 1:방문, 2:cycle

# dfs로 cycle 찾기
def dfs(current, past):
    # retrun 1~n : 사이클을 찾았고, 사이클의 시작점을 반환
    # return 0 : 사이클을 찾지 못함
    # return -1 : 사이클을 찾았고, 현재 정점이 사이클에 포함되지 않음
    if visited[current] == 1:
        return current
    
    visited[current] = 1

    for next in a[current]:
        if next == past:
            continue
        
        ret = dfs(next, current)
        if ret == -1:
            return -1
        if ret >= 1:
            visited[current] = 2
            if current == ret:
                return -2 # 다시 사이클 시작점으로 리턴되면, 지금부터는 사이클에 포함되지 않는 간선들
            else:
                return ret
    return 0


# 순환선 사이의 거리 저장
dist = [-1] * (n+1)
# bfs로 순환선을 이루는 정점에서 다른 정점까지의 거리 구하기
def bfs(cycles):
    q = deque(cycles)
    for x in cycles:
        dist[x] = 0
    
    while q:
        current = q.popleft()
        for next in a[current]:
            if dist[next] == -1:
                q.append(next)
                dist[next] = dist[current] + 1


# 순환선 사이의 거리 저장
# 사이클을 이루는 정점들 저장
cycles = []
# 방문여부
dfs(1, -1) # cycle 찾기
for i in range(1, n+1):
    if visited[i] == 2: #cycle
        cycles.append(i)
bfs(cycles)
print(' '.join(list(map(str, dist[1:]))))