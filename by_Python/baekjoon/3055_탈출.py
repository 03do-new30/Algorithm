import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

start_r = 0; start_c = 0
goal_r = 0; goal_c = 0
waters = []
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'S':
            start_r = r; start_c = c
        elif arr[r][c] == 'D':
            goal_r = r; goal_c = c
        elif arr[r][c] == '*':
            waters.append((r, c))

def flood(waters):
    visited = [[-1] * m for _ in range(n)]
    q = deque(waters)
    for x, y in q:
        visited[x][y] = 0
        # visited[x][y] = t 
        # (x, y)에 물이 차는 시간은 t초
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1 ,1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == '.' and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
    return visited

water_check = flood(waters) # 위치 (r, c)에 물이 차는 시간을 저장

visited = [[-1] * m for _ in range(n)]
q = deque([(start_r, start_c)])
visited[start_r][start_c] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    r, c = q.popleft()
    time = visited[r][c]
    next_time = time + 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] in ['D', '.'] and visited[nr][nc] == -1:
                # 물이 차있지 않거나, 물이 찰 예정이 아니어야 함
                if water_check[nr][nc] == -1 or next_time < water_check[nr][nc]:
                    visited[nr][nc] = next_time
                    q.append((nr, nc))

ans = visited[goal_r][goal_c]
if ans == -1:
    print('KAKTUS')
else:
    print(ans)