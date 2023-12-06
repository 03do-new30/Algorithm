import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

normal_visited = [[False]*n for _ in range(n)]
weak_visited = [[False]*n for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs_normal(r, c):
    q = deque([(r, c)])
    normal_visited[r][c] = True
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == arr[r][c] and not normal_visited[nr][nc]:
                    normal_visited[nr][nc] = True
                    q.append((nr, nc))

def bfs_weak(r, c):
    q = deque([(r, c)])
    weak_visited[r][c] = True
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not weak_visited[nr][nc]:
                    if arr[nr][nc] == 'B':
                        if arr[nr][nc] == arr[r][c]:
                            weak_visited[nr][nc] = True
                            q.append((nr, nc))
                    else:
                        if arr[r][c] in ('R', 'G'):
                            weak_visited[nr][nc] = True
                            q.append((nr, nc))
# normal
normal_count = 0
while True:
    done = True
    for x in range(n):
        for y in range(n):
            if not normal_visited[x][y]:
                done = False
                bfs_normal(x, y)
                normal_count += 1
    if done:
        break
# weak
weak_count = 0
while True:
    done = True
    for x in range(n):
        for y in range(n):
            if not weak_visited[x][y]:
                done = False
                bfs_weak(x, y)
                weak_count += 1
    if done:
        break

print(normal_count, weak_count)