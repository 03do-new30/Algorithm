import sys
input = sys.stdin.readline
from collections import deque

arr = [list(input().strip()) for _ in range(8)]
walls = []
for r in range(8):
    for c in range(8):
        if arr[r][c] == '#':
            walls.append((r, c))

def move_walls(walls):
    new_walls = []
    for r, c in walls:
        nr = r + 1
        if 0 <= nr < 8:
            new_walls.append((nr, c))
    return new_walls

visited = [[[False for _ in range(9)]for __ in range(8)]for ___ in range(8)]
# (r, c, t): t초 후에 (r, c)에 있을 때 최소 시간
q = deque([(7, 0, 0)])
visited[7][0][0] = True
dr = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
dc = [0, 0, -1, 1, -1, 1, -1, 1, 0]
ans = False
while q:
    r, c, t = q.popleft()
    if r == 0 and c == 7:
        break
    for i in range(9):
        nr = r + dr[i]
        nc = c + dc[i]
        nt = min(t + 1, 8)
        if 0 <= nr < 8 and 0 <= nc < 8:
            # 현재 칸이 벽인지 확인
            if 0 <= nr-t and arr[nr-t][nc] == '#':
                continue
            # 이동하려는 칸에 벽이 내려올지 확인
            if 0 <= nr-nt and arr[nr-nt][nc] == '#':
                continue
            # 모두 아니라면 이동하려는 칸은 빈칸
            if not visited[nr][nc][nt]:
                visited[nr][nc][nt] = True
                q.append((nr, nc, nt))

if visited[0][7].count(True) > 0:
    print(1)
else:
    print(0)