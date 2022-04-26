import sys
input = sys.stdin.readline
from collections import deque

def bfs(r, c):
    # 그림의 넓이 width
    width = 1
    q = deque([(r, c)])
    visited[r][c] = True

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    width += 1
    
    return width
    

    


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 그림의 개수 cnt
cnt = 0
# 가장 큰 그림의 넓이
max_width = 0

for r in range(n):
    for c in range(m):
        if arr[r][c] == 1 and not visited[r][c]:
            max_width = max(max_width, bfs(r, c))
            cnt += 1

print(cnt)
print(max_width)