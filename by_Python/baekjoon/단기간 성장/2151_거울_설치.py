import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

# 시작점
start = (-1, -1)
for r in range(n):
    stop = False
    for c in range(n):
        if arr[r][c] == '#':
            start = (r, c)
            stop = True
            break
    if stop:
        break

# 방향: 상,하,좌,우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# visited[r][c][i]: (r, c)에 i방향으로 진입한 적이 있는지 체크
visited = [[[False] * 4 for _ in range(n)] for __ in range(n)]

q = deque([])
for i in range(4):
    visited[start[0]][start[1]][i] = True
    q.append((start[0], start[1], i, 0)) # (r, c, 방향, 가중치)

# 0-1 BFS
# 거울을 설치하는 경우 가중치 + 1 -> 큐의 뒤에 삽입
# 거울을 설치하지 않는 경우 가중치 + 0 -> 큐의 앞에 삽입
ans = float('inf')
while q:
    r, c, dir, wt = q.popleft()

    # 도착점에 도달한 경우
    if arr[r][c] == '#' and (r != start[0] or c != start[1]):
        ans = wt
        # 0-1 BFS로 풀었으므로 처음 나온 답이 무조건 최소 거울 개수
        break

    # 빛은 거울과 만나지 않는 이상 이전 진행 방향을 유지하며 직진한다.
    nr = r + dr[dir]
    nc = c + dc[dir]

    # 범위 밖
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        continue

    # 방문
    if visited[nr][nc][dir]:
        continue

    # [1] 벽
    if arr[nr][nc] == '*':
        continue

    # [2] 거울
    if arr[nr][nc] == '!':
        visited[nr][nc][dir] = True
        # (1) 거울을 설치하는 경우
        # 0-1 BFS: 거울을 설치하는 경우 큐 뒤에 삽입
        # 기존 진행 방향 상/하 -> 좌/우 빛 반사 가능
        if dir == 0 or dir == 1:
            q.append((nr, nc, 2, wt + 1))
            q.append((nr, nc, 3, wt + 1))
        # 기존 진행 방향 좌/우 -> 상/하 빛 반사 가능
        else:
            q.append((nr, nc, 0, wt + 1))
            q.append((nr, nc, 1, wt + 1))
        # (2) 거울을 설치하지 않는 경우
        q.appendleft((nr, nc, dir, wt))
    # [3] 빛이 통과할 수 있는 곳 (빈칸/도착점 문)
    else:
        visited[nr][nc][dir] = True
        q.appendleft((nr, nc, dir, wt))

print(ans)