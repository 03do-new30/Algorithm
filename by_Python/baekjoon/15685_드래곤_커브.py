import sys
input = sys.stdin.readline

arr = [[0]*(101) for _ in range(101)]
dirs = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}


def dragon(g):
    dragon_dir = []

    while g >= 0:
        # dragon_dir가 비어있는 경우 (시작)
        if len(dragon_dir) == 0:
            dragon_dir.append(d)
        # dragon_dir 수정해주기
        else:
            dragon_dir = next_dragon_dir(dragon_dir)

        g -= 1

    return dragon_dir


def next_dragon_dir(dragon_dir):
    # 0세대 드래곤커브 (0, 1)
    # 1세대 드래곤커브, (-1, 0)이 추가됨

    # 1세대 드래곤커브가 (0, 1), (-1, 0*)이었는데
    # 2세대 드래곤커브, (0, -1*), (-1, 0)가 추가됨

    # 2세대 드래곤커브 0:(*0, 1), 1:(-1, 0*), 2:(0, -1), 1:(-1, 0)
    # 3세대 드래곤커브, 2:(0, -1), 3:(1, 0), 2:(0, -1*), 1:(*-1, 0) 추가됨
    new_dragon_dir = list(reversed(dragon_dir))
    for i in range(len(new_dragon_dir)):
        if new_dragon_dir[i] == 3:
            new_dragon_dir[i] = 0
        else:
            new_dragon_dir[i] += 1
    return dragon_dir + new_dragon_dir


def is_square(r, c):
    # r, c에서 →, ↓, ← 방향을 검사했을 때
    # 네 방향이 모두 1이면 1 * 1 정사각형의 네 꼭지점이 모두 커브의 일부
    count = 1  # 일단 (r, c)가 1이므로 count 1로 시작한다
    moves = [(0, 1), (1, 0), (0, -1)]
    for move in moves:
        n_r = r + move[0]
        n_c = c + move[1]
        if 0 <= n_r < 101 and 0 <= n_c < 101:
            if arr[n_r][n_c] == 1:
                count += 1
                r = n_r
                c = n_c
            else:
                return False
        else:
            return False

    if count == 4:
        return True
    else:
        return False

    # x좌표가 arr에서의 col, y좌표가 arr에서의 row임에 유의한다
for _ in range(int(input().strip())):
    col, row, d, g = map(int, input().split())
    dragon_dir = dragon(g)
    # (row, col)에서 시작해서 dragon_dir의 방향들로 이동하며
    # arr을 1로 바꾸어간다
    # 시작점
    arr[row][col] = 1

    for direction in dragon_dir:
        d_row, d_col = dirs[direction]
        n_row = row + d_row
        n_col = col + d_col
        arr[n_row][n_col] = 1
        # update
        row = n_row
        col = n_col

ans = 0
for r in range(101):
    for c in range(101):
        if arr[r][c] == 1:
            if is_square(r, c):
                ans += 1

print(ans)
