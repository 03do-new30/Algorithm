import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def mark_air(arr):
    # 치즈의 구멍과, 바깥 공기를 구분하기 위해
    # arr에서 치즈 바깥에 있는 공기들을 -1로 표시한다
    # (0, 0)은 항상 공기이므로, 시작점으로 잡는다
    visited = [[False]*m for _ in range(n)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    q = deque([(0, 0)])
    visited[0][0] = True
    arr[0][0] = -1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc]
                    q.append((nr, nc))
                    arr[nr][nc] = -1


def melt(arr):
    mark_air(arr)
    new_arr = [row[:] for row in arr]

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    # 상, 하, 좌, 우로 바깥 공기와 접촉 시
                    if arr[nr][nc] == -1:
                        new_arr[r][c] = 0
                        break

    # -1로 마크해놓은 바깥 공기 다시 0으로 돌림
    for r in range(n):
        for c in range(m):
            if new_arr[r][c] == -1:
                new_arr[r][c] = 0

    return new_arr


def count_chesses(arr):
    cnt = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                cnt += 1
    return cnt


def no_cheese(arr):
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                return False
    return True


ans = 0
while True:
    new_arr = melt(arr)
    ans += 1
    """
    print('-'*30)
    for row in new_arr:
        print(row)
    print('-'*30)
    """
    if no_cheese(new_arr):
        print(ans)
        print(count_chesses(arr))
        break

    # update
    arr = [row[:] for row in new_arr]
