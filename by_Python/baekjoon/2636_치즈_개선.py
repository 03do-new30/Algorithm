import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def melt(arr):
    # 치즈가 녹은 후의 상태
    new_arr = [row[:] for row in arr]

    # 공기에 접촉하는 치즈 녹이기
    air_cheese = get_air_cheese(arr)

    while air_cheese:
        r, c = air_cheese.popleft()
        new_arr[r][c] = 0

    return new_arr


def get_air_cheese(arr):
    # 공기에 접촉하는 치즈의 위치 구하기
    air_cheese = deque([])

    visited = [[False]*m for _ in range(n)]
    # (0, 0)에서 탐색 시작
    q = deque([(0, 0)])
    visited[0][0] = True

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True

                # 공기와 접촉하는 치즈의 위치
                elif arr[nr][nc] == 1 and not visited[nr][nc]:
                    air_cheese.append((nr, nc))
                    visited[nr][nc] = True
    return air_cheese


def all_melt(arr):
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                return False
    return True


def count_cheese(arr):
    ans = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                ans += 1
    return ans


ans = 0  # 걸리는 시간
while True:
    new_arr = melt(arr)
    ans += 1

    # 다 녹았는가?
    if all_melt(new_arr):
        print(ans)
        # 녹기 한시간 전 치즈조각 개수
        print(count_cheese(arr))
        break

    # update
    arr = [row[:] for row in new_arr]
