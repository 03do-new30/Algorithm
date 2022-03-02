import sys
input = sys.stdin.readline


def count(arr):
    # 가장 긴 행 또는 열의 연속 부분을 구한다
    max_cnt = 0

    # 행
    for row in range(N):
        prev = arr[row][0]
        cnt = 1
        for col in range(1, N):
            if arr[row][col] == prev:
                cnt += 1
            else:
                cnt = 1  # reset
                prev = arr[row][col]

            # 현재까지의 cnt가 max_cnt보다 크면 갱신
            max_cnt = max(max_cnt, cnt)

    # 열
    for col in range(N):
        prev = arr[0][col]
        cnt = 1
        for row in range(1, N):
            if arr[row][col] == prev:
                cnt += 1
            else:
                cnt = 1  # reset
                prev = arr[row][col]

            # 현재까지의 cnt가 max_cnt보다 크면 갱신
            max_cnt = max(max_cnt, cnt)

    return max_cnt


N = int(input().strip())
arr = [list(input().strip()) for _ in range(N)]  # 사탕이 채워진 상태

# 아래쪽, 오른쪽만 검사하면 된다
# e.g., (r, c)와 그 우측을 교체한 것 = (r, c+1)과 그 좌측을 교체한 것
dr = [0, 1]
dc = [1, 0]

max_ans = 0

for r in range(N):
    for c in range(N):
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                # 사탕의 색이 다른 인접한 두 칸을 고른다
                if arr[r][c] != arr[nr][nc]:
                    # 교체
                    arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                    # 카운트
                    max_ans = max(max_ans, count(arr))
                    # 교체
                    arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]

print(max_ans)
