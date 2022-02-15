import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def route(r, c, dr, dc):

    # 경사로를 놓은 곳을 표시
    visited = [[False]*N for _ in range(N)]

    while 0 <= r + dr < N and 0 <= c + dc < N:
        """ debugging
        print("r:", r, "c:", c, "| r + dr:", r+dr, "c+dc:", c+dc)
        """
        if arr[r][c] == arr[r+dr][c+dc]:
            r += dr
            c += dc

        # 다음 블록이 낮은 블록
        elif arr[r][c] - arr[r+dr][c+dc] == 1:
            slide = lower_block(r, c, dr, dc, visited)
            if slide:
                # 경사로를 설치할 수 있음
                # visited에 표시한다
                nr = r
                nc = c
                for _ in range(L):
                    nr += dr
                    nc += dc
                    visited[nr][nc] = True

                # 경사로를 놓은 뒤의 블록으로 이동
                r += dr*L
                c += dc*L
            else:
                # 경사로를 설치할 수 없음
                return False

        # 다음 블록이 높은 블록
        elif arr[r][c] - arr[r+dr][c+dc] == -1:
            # lower_block과 달리 높은 블록의 위치를 인자로 줌에 주의
            slide = higher_block(r+dr, c+dc, dr, dc, visited)
            if slide:
                # 경사로를 설치할 수 있음
                # visited에 표시한다
                nr = r + dr
                nc = c + dc
                for _ in range(L):
                    nr -= dr
                    nc -= dc
                    visited[nr][nc] = True
                # 뒤에 경사로를 놓았으므로 다음 위치는 그냥 + dr, + dc
                r += dr
                c += dc
            else:
                # 경사로를 설치할 수 없음
                return False

        else:
            return False

    return True


def lower_block(r, c, dr, dc, visited):
    # 원래 r, c의 높이
    height = arr[r][c]

    # L개의 칸이 연속되어 있는가?
    if 0 <= r + dr*L < N and 0 <= c + dc*L < N:
        # L개의 칸의 높이가 모두 height - 1인가?
        new_r = r
        new_c = c
        for _ in range(L):
            new_r += dr
            new_c += dc
            # 칸의 높이가 height - 1이 아님
            if arr[new_r][new_c] != height - 1:
                return False
            # 이미 경사로가 설치되어 있음
            if visited[new_r][new_c]:
                return False
    else:
        # L개의 칸이 연속되어 있지 않음
        return False

    return True


def higher_block(higher_r, higher_c, dr, dc, visited):
    # 한 칸 더 높은 [higher_r][higher_c]의 높이
    height = arr[higher_r][higher_c]

    # (higher_r, higher_c)의 왼쪽으로 L개의 칸이 연속되어 있는가?
    if 0 <= higher_r - dr*L < N and 0 <= higher_c - dc*L < N:
        # L개의 칸의 높이가 모두 height - 1인가?
        new_r = higher_r
        new_c = higher_c
        for _ in range(L):
            new_r -= dr
            new_c -= dc
            # 칸의 높이가 height - 1이 아님
            if arr[new_r][new_c] != height - 1:
                return False
            # 이미 경사로가 설치되어 있음
            if visited[new_r][new_c]:
                return False
    else:
        # L개의 칸이 연속되어 있지 않음
        return False

    return True


# 답
ans = 0

# arr[0][0], arr[0][1], ... arr[0][N-1]에서 아래방향으로 검사
for c in range(N):
    is_route = route(0, c, 1, 0)
    if is_route:
        ans += 1

# arr[0][0], arr[1][0], ... arr[N-1][0]에서 오른쪽방향으로 검사
for r in range(N):
    is_route = route(r, 0, 0, 1)
    if is_route:
        ans += 1

print(ans)
