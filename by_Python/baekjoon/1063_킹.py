import sys
from collections import deque
input = sys.stdin.readline


def location(string):
    # A2 -> board[7][1]로 쓸 수 있게 변환
    row = 9 - int(string[1])
    col = ord(string[0]) - 64
    return (row, col)


def location_reverse(row, col):
    # board[7][1] -> A2로 변환
    number = 9 - row
    alphabet = chr(64 + col)
    return alphabet+str(number)


board = [[0]*9 for _ in range(9)]
# 입력
king, stone, move = input().split()
# board에 king, stone 표시
king_row, king_col = location(king)
stone_row, stone_col = location(stone)
board[king_row][king_col] = 1  # 1 = king
board[stone_row][stone_col] = 2  # 2 = stone
# move 정보 받기
move_cmd = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
            'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}
moves = deque([])
for _ in range(int(move)):
    moves.append(move_cmd[input().strip()])


def move_king(r, c):
    while moves:
        r_move, c_move = moves.popleft()
        new_r = r + r_move
        new_c = c + c_move

        if test_safe_inex(new_r, new_c):
            # 돌과 같은 곳으로 이동한다면
            if board[new_r][new_c] == 2:
                # 돌을 같은 방향으로 한 칸 이동하는데,
                # 이 때 돌의 인덱스 체크
                stone_r = new_r + r_move
                stone_c = new_c + c_move
                if test_safe_inex(stone_r, stone_c):
                    # 이동
                    board[stone_r][stone_c] = 2
                    board[new_r][new_c] = 1
                    board[r][c] = 0  # 이전 위치 비워주기
                    # r, c 업데이트
                    r = new_r
                    c = new_c
                # safe_index가 아니라면 아무 동작도 하지 않음
                else:
                    continue
            # 빈칸으로 이동한다면
            else:
                board[new_r][new_c] = 1
                board[r][c] = 0
                # r, c 업데이트
                r = new_r
                c = new_c
        # safe_index가 아니라면 아무 동작도 하지 않음
        else:
            continue
        """
        print('='*15, r_move, c_move, '='*15)
        for row in board:
            print(row)
        """


def test_safe_inex(r, c):
    if 1 <= r <= 8 and 1 <= c <= 8:
        return True
    return False


def get_king_loc():
    for r in range(1, 9):
        for c in range(1, 9):
            if board[r][c] == 1:
                return (r, c)


def get_stone_loc():
    for r in range(1, 9):
        for c in range(1, 9):
            if board[r][c] == 2:
                return (r, c)


# move_king 실행
move_king(king_row, king_col)
# king의 위치, stone의 위치를 출력
king_row, king_col = get_king_loc()
stone_row, stone_col = get_stone_loc()
print(location_reverse(king_row, king_col))
print(location_reverse(stone_row, stone_col))
