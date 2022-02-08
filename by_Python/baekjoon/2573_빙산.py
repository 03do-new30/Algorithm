import sys
from collections import deque
input = sys.stdin.readline


def melt(r, c, arr):
    d_r = [0, 0, -1, 1]
    d_c = [-1, 1, 0, 0]
    cnt = 0  # 바닷물에 접하는 부분의 개수

    for i in range(4):
        n_r = r + d_r[i]
        n_c = c + d_c[i]
        if arr[n_r][n_c] == 0:
            cnt += 1

    # 녹은 뒤의 빙산 높이
    ret = arr[r][c] - cnt
    if ret < 0:
        return 0
    return ret


def bfs(r, c, arr, visited):
    d_r = [0, 0, -1, 1]
    d_c = [-1, 1, 0, 0]
    q = deque([(r, c)])
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r = r + d_r[i]
            n_c = c + d_c[i]

            # (n_r, n_c)가 빙산
            if arr[n_r][n_c] > 0 and not visited[n_r][n_c]:
                q.append((n_r, n_c))
                visited[n_r][n_c] = True


# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    # 빙산이 분리되는지 체크
    visited = [[False]*M for _ in range(N)]
    bfs_count = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0 and not visited[r][c]:
                bfs(r, c, arr, visited)
                bfs_count += 1

    # 빙산이 분리된다
    if bfs_count > 1:
        print(ans)
        break

    # 빙산이 다 녹았는지 체크
    all_melt = True
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                all_melt = False
                break

    if all_melt:
        print(0)
        break

    # ice: 빙산의 위치를 저장하는 리스트
    ice = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                ice.append((r, c))

    # 현재 arr의 빙산을 녹인 후의 상태를 저장하는 리스트 new_arr
    new_arr = [[0]*M for _ in range(N)]
    for info in ice:
        r, c = info
        new_arr[r][c] = melt(r, c, arr)

    # new_arr의 상태를 arr에 다시 저장
    arr = [row[:] for row in new_arr]

    # ans 증가
    ans += 1
