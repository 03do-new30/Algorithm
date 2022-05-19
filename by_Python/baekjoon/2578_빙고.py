import sys
input = sys.stdin.readline

def check_num(n):
    for r in range(5):
        for c in range(5):
            if arr[r][c] == n:
                arr[r][c] = -1
                find_bingo(r, c)
                return

def find_bingo(row, col):
    # (row, col) 지점에서 빙고가 완성되는 줄이 있는지 탐색한다
    global bingo_count

    # 가로
    row_bingo = True
    for c in range(5):
        if arr[row][c] != -1:
            row_bingo = False
            break
    
    if row_bingo:
        bingo_count += 1
    
    # 세로
    col_bingo = True
    for r in range(5):
        if arr[r][col] != -1:
            col_bingo = False
            break
    
    if col_bingo:
        bingo_count += 1
    
    # \
    backslash_bingo = True
    if (row, col) in backslashes:
        for r, c in backslashes:
            if arr[r][c] != -1:
                backslash_bingo = False
                break
        
        if backslash_bingo:
            bingo_count += 1
        
        
    # /
    slash_bingo = True
    if (row, col) in slashes:
        for r, c in slashes:
            if arr[r][c] != -1:
                slash_bingo = False
                break
        
        if slash_bingo:
            bingo_count += 1



arr = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
call_count = 0
bingo_count = 0
backslashes = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
slashes = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]

done = False

for i in range(5):
    if done:
        break
    for j in range(5):
        call_count += 1
        check_num(call[i][j])
        if bingo_count >= 3:
            print(call_count)
            done = True
            break
        