import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[[0 for _ in range(k+1)] for __ in range(m)] for ___ in range(n)]

# (0, 0)에서 출발
q = deque([(0, 0, 0)])
visited[0][0][0] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while q:
    r, c, wall = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            # 빈칸인 경우
            if arr[nr][nc] == 0:
                if visited[nr][nc][wall] == 0:
                    visited[nr][nc][wall] = visited[r][c][wall] + 1
                    q.append((nr, nc, wall))
            # 벽인 경우
            else:
                if wall + 1 <= k and visited[nr][nc][wall+1] == 0:
                    visited[nr][nc][wall + 1] = visited[r][c][wall] + 1
                    q.append((nr, nc, wall + 1))

shortest = -1
for x in visited[n-1][m-1]:
    if x > 0:
        if shortest == -1:
            shortest = x
        else:
            shortest = min(x, shortest)
print(shortest)