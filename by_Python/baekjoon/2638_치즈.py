import sys
from collections import deque
import copy
input = sys.stdin.readline

# (0, 0)에서 bfs, 1을 만나면 바깥공기와 접촉하는 치즈조각


def melt(arr):
    q = deque([(0, 0)])
    # visited 표시
    # 방문X : -1
    # 공기  : 0
    # 치즈  : 공기와의접촉횟수(>= 1)
    visited = [[-1]*M for _ in range(N)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                # 공기
                if arr[nr][nc] == 0:
                    if visited[nr][nc] == -1:
                        visited[nr][nc] = 0
                        q.append((nr, nc))
                # 치즈
                elif arr[nr][nc] == 1:
                    if visited[nr][nc] == -1:
                        visited[nr][nc] = 1
                    else:
                        visited[nr][nc] += 1

    # visited[r][c] >= 2인 치즈들은 제거한다
    new_arr = copy.deepcopy(arr)
    for r in range(N):
        for c in range(M):
            if visited[r][c] >= 2:
                new_arr[r][c] = 0
    return new_arr


def all_melt(arr):
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                return False
    return True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while not all_melt(arr):
    arr = melt(arr)
    ans += 1

print(ans)
