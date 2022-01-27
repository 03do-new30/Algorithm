import sys
from collections import deque
input = sys.stdin.readline

# 입력
n = int(input().strip())
# 보드의 상하좌우 끝 벽 = -1
# 빈 칸 = 0
# 사과 = 1
board = [[-1]*(n+2)] + [[-1] + [0]*n + [-1] for _ in range(n)] + [[-1]*(n+2)]
# 사과 입력
k = int(input().strip())
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1
# 방향 변환 정보 입력
L = int(input().strip())
dir_cmd = dict()
for _ in range(L):
    x, c = input().split()
    dir_cmd[int(x)] = c


def move_snake(row, col, dir, snake_body, time):
    while True:
        """
        print('='*30)
        print("현재 초", time)
        print("뱀의 궤적", snake_body)
        print('='*30)
        for _ in board:
            print(_)
        """

        # 방향 전환
        if time in dir_cmd and dir_cmd[time] == 'L':
            # print("왼쪽으로 방향전환해욧")
            # (0, 1) -> (-1, 0)
            # (0, -1) -> (1, 0)
            # (1, 0) -> (0, 1)
            # (-1, 0) -> (0, -1)
            dir = [-dir[1], dir[0]]
        elif time in dir_cmd and dir_cmd[time] == 'D':
            # print("오른쪽으로 방향전환해욧")
            # (0, 1) -> (1, 0)
            # (0, -1) -> (-1, 0)
            # (1, 0) -> (0, -1)
            # (-1, 0) -> (0, 1)
            dir = [dir[1], -dir[0]]
        next_row = row + dir[0]
        next_col = col + dir[1]

        # 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다
        if board[next_row][next_col] == -1 or (next_row, next_col) in snake_body:
            # 다음 이동 시 게임이 끝날 것이므로 time + 1
            return time+1

        # 이동한 칸에 사과가 있다
        if board[next_row][next_col] == 1:
            # 사과 없애주기
            board[next_row][next_col] = 0
            # 업데이트
            row = next_row
            col = next_col
            snake_body.append((row, col))
        # 이동한 칸에 사과가 없다
        else:
            # 꼬리가 위치한 칸을 비워준다
            tail_row, tail_col = snake_body.popleft()
            # 업데이트
            row = next_row
            col = next_col
            snake_body.append((row, col))

        time += 1


# 초기 뱀의 위치는 (1, 1)
# snake_body = 뱀의 지금까지 궤적을 저장한 큐
# snake_body의 길이가 뱀의 길이
snake_body = deque([(1, 1)])
# 초기 dir는 오른쪽
print(move_snake(1, 1, [0, 1], snake_body, 0))
