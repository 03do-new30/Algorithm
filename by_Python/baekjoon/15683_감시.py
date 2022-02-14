import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def cctv(arr, r, c, dx, dy):
    new_arr = [row[:] for row in arr]
    # dx = [0, 0, -1, 1]
    # dy = [-1, 1, 0, 0]
    for i in range(len(dx)):
        new_r = r
        new_c = c
        while 0 <= new_r + dx[i] < N and 0 <= new_c + dy[i] < M:
            new_r += dx[i]
            new_c += dy[i]
            # 빈칸이라면
            if new_arr[new_r][new_c] == 0:
                new_arr[new_r][new_c] = -1  # -1을 감시하는 구역으로 표시
            # 다른 cctv라면
            elif 0 <= new_arr[new_r][new_c] < 6:
                continue  # 통과
            # 벽이라면
            elif new_arr[new_r][new_c] == 6:
                break  # 중단
    return new_arr


def solve(arr, q):
    global min_area

    # q가 비어있을 경우
    if len(q) == 0:
        tmp_area = 0
        for r in range(N):
            for c in range(M):
                if arr[r][c] == 0:
                    tmp_area += 1
        min_area = min(min_area, tmp_area)
        return

    r, c = q.popleft()
    if arr[r][c] == 1:
        arr_left = cctv(arr, r, c, [0], [-1])
        arr_right = cctv(arr, r, c, [0], [1])
        arr_bottom = cctv(arr, r, c, [1], [0])
        arr_top = cctv(arr, r, c, [-1], [0])
        # recursion
        # q를 항상 deepcopy 해줘야 함에 유의
        solve(arr_left, deque([x for x in q]))
        solve(arr_right, deque([x for x in q]))
        solve(arr_bottom, deque([x for x in q]))
        solve(arr_top, deque([x for x in q]))

    elif arr[r][c] == 2:
        arr_left_right = cctv(arr, r, c, [0, 0], [-1, 1])
        arr_top_bottom = cctv(arr, r, c, [-1, 1], [0, 0])
        # recursion
        solve(arr_left_right, deque([x for x in q]))
        solve(arr_top_bottom, deque([x for x in q]))

    elif arr[r][c] == 3:
        arr_top_right = cctv(arr, r, c, [-1, 0], [0, 1])
        arr_right_bottom = cctv(arr, r, c, [0, 1], [1, 0])
        arr_bottom_left = cctv(arr, r, c, [1, 0], [0, -1])
        arr_left_top = cctv(arr, r, c, [0, -1], [-1, 0])
        # recursion
        solve(arr_top_right, deque([x for x in q]))
        solve(arr_right_bottom, deque([x for x in q]))
        solve(arr_bottom_left, deque([x for x in q]))
        solve(arr_left_top, deque([x for x in q]))

    elif arr[r][c] == 4:
        arr_not_bottom = cctv(arr, r, c, [-1, 0, 0], [0, 1, -1])
        arr_not_left = cctv(arr, r, c, [-1, 0, 1], [0, 1, 0])
        arr_not_top = cctv(arr, r, c, [0, 0, 1], [-1, 1, 0])
        arr_not_right = cctv(arr, r, c, [-1, 0, 1], [0, -1, 0])
        # recursion
        solve(arr_not_bottom, deque([x for x in q]))
        solve(arr_not_left, deque([x for x in q]))
        solve(arr_not_top, deque([x for x in q]))
        solve(arr_not_right, deque([x for x in q]))

    elif arr[r][c] == 5:
        new_arr = cctv(arr, r, c, [0, 0, -1, 1], [-1, 1, 0, 0])
        # recursion
        solve(new_arr, deque([x for x in q]))


# cctv의 좌표 저장
q = deque([])
for r in range(N):
    for c in range(M):
        if 0 < arr[r][c] < 6:
            q.append((r, c))

min_area = 64

solve(arr, q)
print(min_area)
