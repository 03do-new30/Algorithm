import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]


def move_board(board, dx, dy):
    # return할 새로운 상태의 보드
    new_board = [[0]*N for _ in range(N)]

    # 합쳐졌는지 여부를 표시하는 collision
    collision = [[False]*N for _ in range(N)]

    # 위로 옮기면 가장 위 row부터,
    # 아래로 옮길 때는 가장 아래 row부터,
    # 왼쪽으로 옮길 때는 가장 좌측 col부터,
    # 오른쪽으로 옮길 때는 가장 우측 col부터 움직여야 한다.

    # 위, 아래
    if dy == 0:
        # 위
        if dx == -1:
            row_range = range(N)
        # 아래
        elif dx == 1:
            row_range = range(N-1, -1, -1)

        for r in row_range:
            for c in range(N):
                if board[r][c] != 0:
                    move_block(board, dx, dy, r, c, new_board, collision)

    # 왼쪽, 오른쪽
    elif dx == 0:
        # 왼쪽
        if dy == -1:
            col_range = range(N)
        # 오른쪽
        elif dy == 1:
            col_range = range(N-1, -1, -1)

        for c in col_range:
            for r in range(N):
                if board[r][c] != 0:
                    move_block(board, dx, dy, r, c, new_board, collision)

    return new_board


def move_block(board, dx, dy, r, c, new_board, collision):
    new_r = r
    new_c = c

    while 0 <= new_r + dx < N and 0 <= new_c + dy < N:
        new_r += dx
        new_c += dy
        # 빈칸이 아니라면 중단
        if new_board[new_r][new_c] != 0:
            break

    while True:
        # 숫자가 같고, (new_r, new_c)가 합쳐진 적이 없으면 합쳐짐
        if new_board[new_r][new_c] == board[r][c] and not collision[new_r][new_c]:
            new_board[new_r][new_c] += board[r][c]
            # 합쳐졌음을 표시
            collision[new_r][new_c] = True
            break

        # 빈칸을 만나면 그자리에 들어감
        if new_board[new_r][new_c] == 0:
            new_board[new_r][new_c] = board[r][c]
            break

        # 왔던 방향의 반대로 되돌아감
        new_r -= dx
        new_c -= dy


def solve(board, cnt):
    global max_block

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if cnt == 5:
        current_max = max(map(max, board))
        max_block = max(max_block, current_max)
        return

    for move in moves:
        dx, dy = move
        new_board = move_board(board, dx, dy)
        solve(new_board, cnt + 1)


max_block = 0
solve(board, 0)
print(max_block)
