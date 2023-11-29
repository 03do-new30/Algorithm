import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

MAX = float('inf')
visited = [[[MAX]*(k+1) for __ in range(m)] for ___ in range(n)]
visited[0][0][k] = 0
q = deque([(0, 0, 1, k)])
result = MAX
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while q:
    r, c, t, left = q.popleft()
    if (r, c) == (n-1, m-1):
        result = min(result, t)
        continue
    
    daytime = t % 2 # 1이면 낮 0이면 밤

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            # 빈칸인 경우
            if arr[nr][nc] == 0:
                # 이동하는 경우
                if visited[nr][nc][left] > t:
                    visited[nr][nc][left] = t
                    q.append((nr, nc, t + 1, left))
            # 벽인 경우
            else:
                # 현재 낮인 경우, 벽 부수기 가능
                if left and visited[nr][nc][left-1] > t:
                    if daytime:
                        visited[nr][nc][left-1] = t
                        q.append((nr, nc, t+1, left-1))
                    else:
                        q.append((r, c, t+1, left))

print(result if result < MAX else -1)