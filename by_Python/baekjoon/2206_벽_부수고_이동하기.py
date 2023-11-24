import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

def bfs():
    # visited[r][c][0] = 벽을 부수지 않은 상태
    # visited[r][c][1] = 벽을 부순 상태
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0, 0)]) #(행, 열, 벽 부수지 않으면 0이고 부순 상태이면 1)
    visited[0][0][0] = 1 # 시작하는 칸도 포함해서 센다

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c, destroy = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                # 빈공간
                if arr[nr][nc] == 0:
                    if visited[nr][nc][destroy] == 0:
                        visited[nr][nc][destroy] = visited[r][c][destroy] + 1
                        q.append((nr, nc, destroy))
                # 벽
                else:
                    # 벽을 부수지 않은 상태여야 한다
                    if destroy == 0:
                        visited[nr][nc][1] = visited[r][c][0] + 1
                        q.append((nr, nc, 1))
    
    return (visited[n-1][m-1][0], visited[n-1][m-1][1])


ans = bfs()
if 0 in ans:
    min_dist = max(ans)
else:
    min_dist = min(ans)

if min_dist == 0:
    print(-1)
else:
    print(min_dist)