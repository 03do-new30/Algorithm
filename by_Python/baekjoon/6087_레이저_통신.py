import sys
input = sys.stdin.readline
from collections import deque

w, h = map(int, input().split())
arr = [list(input().strip()) for _ in range(h)]

# c 찾기
points = []
for r in range(h):
    for c in range(w):
        if arr[r][c] == 'C':
            points.append((r, c))
start = points[0]
goal = points[1]

# 거울 = 직선의 방향을 바꾸는 것
# 거울의 개수 = 두 C를 연결하는 데 필요한 직선의 최소 개수 -1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
q = deque([(start[0], start[1])])
visited = [[-1] * w for _ in range(h)]
visited[start[0]][start[1]] = 0

while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        ok = False
        while 0 <= nr < h and 0 <= nc < w:
            if arr[nr][nc] == '*':
                break
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
            nr += dr[i]
            nc += dc[i]

print(visited[goal[0]][goal[1]] - 1)