import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# dist[r][c] = (r, c)의 최단거리 중 가장 큰 값


def bfs(r, c):
    q = deque([(r, c)])
    # tmp_dist[r][c] == -1이면 방문 X
    tmp_dist = [[-1]*m for _ in range(n)]
    tmp_dist[r][c] = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 'L' and tmp_dist[nr][nc] == -1:
                    q.append((nr, nc))
                    tmp_dist[nr][nc] = tmp_dist[r][c] + 1
                    dist[nr][nc] = max(dist[nr][nc], tmp_dist[nr][nc])


dist = [[-1]*m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'L':
            bfs(r, c)

print(max(map(max, dist)))
