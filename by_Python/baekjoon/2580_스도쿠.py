import sys
input = sys.stdin.readline

arr = [[0] * 9 for _ in range(9)]
row_check = [[False] * 10 for _ in range(9)] # i행에 숫자 j 존재?
col_check = [[False] * 10 for _ in range(9)] # i열에 숫자 j 존재?
box_check = [[False] * 10 for _ in range(9)] # i번째 박스에 숫자 j 존재?

for r in range(9):
    tmp = list(map(int, input().split()))
    for c in range(9):
        arr[r][c] = tmp[c]
        if arr[r][c] != 0:
            num = arr[r][c]
            row_check[r][num] = True
            col_check[c][num] = True
            box_check[(r // 3) * 3 + c // 3][num] = True

def solve(idx):
    if idx == 81:
        for r in range(9):
            print(' '.join(list(map(str, arr[r]))))
        return True
    
    row = idx // 9
    col = idx % 9
    box = (row // 3) * 3 + col // 3
    if arr[row][col] != 0:
        return solve(idx + 1)
    
    for n in range(1, 10):
        if not row_check[row][n] and not col_check[col][n] and not box_check[box][n]:
            row_check[row][n] = True
            col_check[col][n] = True
            box_check[box][n] = True
            arr[row][col] = n
            if solve(idx + 1):
                return True
            row_check[row][n] = False
            col_check[col][n] = False
            box_check[box][n] = False
            arr[row][col] = 0

solve(0)