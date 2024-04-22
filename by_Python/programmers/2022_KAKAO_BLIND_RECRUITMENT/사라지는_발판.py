dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = float('inf')

def solution(board, aloc, bloc):
    return solve(board, aloc, bloc)[1]

def in_range(board, r, c):
    n = len(board); m = len(board[0])
    if 0 <= r < n and 0 <= c < m:
        return True
    return False
    
def is_finished(board, y, x):
    for i in range(4):
        ny = y + dr[i]
        nx = x + dc[i]
        if in_range(board, ny, nx) and board[ny][nx]:
            return False
    return True

def solve(board, my_loc, your_loc): # -> (승패여부, 움직임)
    r, c = my_loc
    ur, uc = your_loc

    # [1] 못움직이는 경우
    if is_finished(board, r, c):
        return (False, 0)
    # [2] 위치가 겹치는 경우, 이번 턴에 움직이는 사람이 이김
    if r == ur and c == uc:
        return (True, 1)
    
    min_turn = INF
    max_turn = 0
    can_win = False

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if in_range(board, nr, nc):
            if board[nr][nc] == 1:
                board[r][c] = 0
                ret_success, ret_cnt = solve(board, your_loc, (nr, nc))
                board[ur][uc] = 1

                if not ret_success:
                    can_win = True
                    min_turn = min(min_turn, ret_cnt)
                else:
                    # 상대가 성공하고
                    # 내가 can_win = False인 경우
                    if not can_win:
                        max_turn = max(max_turn, ret_cnt)
    turn = min_turn if can_win else max_turn
    return (can_win, turn + 1)

board = [
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]	,
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]]	,
    [[1, 1, 1, 1, 1]]	,
    [[1]]	,
    [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
]
aloc = [[1, 0], [1, 0], [0, 0], [0, 0], [0, 0]]
bloc = [[1, 2], [1, 2], [0, 4], [0, 0], [3, 3]]
result = [5, 4, 4, 0, 8]
for i in range(len(result)):
    print(solution(board[i], aloc[i], bloc[i]) == result[i])
    print('-' * 30)