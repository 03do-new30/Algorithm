# 참고: https://www.acmicpc.net/source/15002633 (ydh2244님 코드)
import sys
import copy
input = sys.stdin.readline


def dfs(idx, arr):
    global min_area

    if idx == len(cctv):
        # 모든 cctv 완료
        current_area = sum([row.count(0) for row in arr])
        min_area = min(min_area, current_area)
        return

    r, c, cctv_mode = cctv[idx]

    for cctv_dirs in directions[cctv_mode]:
        new_arr = copy.deepcopy(arr)
        for i in cctv_dirs:
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                # 벽을 만나면
                if new_arr[nr][nc] == 6:
                    break
                if new_arr[nr][nc] == 0:
                    # 빈 공간이라면
                    new_arr[nr][nc] = -1  # 감시할 수 있음을 표시
                # 다른 cctv라면
                # update
                nr += dr[i]
                nc += dc[i]
        dfs(idx+1, new_arr)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
# directions[i] = i번 cctv의 감시 방향들을 저장한 리스트
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[2, 1], [1, 3], [3, 0], [0, 2]],
    [[0, 1, 2], [1, 2, 3], [0, 1, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]


min_area = M*N
cctv = []
for r in range(N):
    for c in range(M):
        if 1 <= arr[r][c] <= 5:
            # cctv가 있는 곳의 row, col, cctv번호를 추가
            cctv.append((r, c, arr[r][c]))

dfs(0, arr)
print(min_area)
