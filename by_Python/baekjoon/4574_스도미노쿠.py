import sys
input = sys.stdin.readline

def to_row_col(string):
    r = string[0]
    c = int(string[1])
    return ord(r) - 65, c - 1

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solve(idx):
    if idx == 81:
        for row in arr:
            print(''.join(list(map(str, row))))
        return True
    
    row = idx // 9
    col = idx % 9
    box = (row // 3) * 3 + col // 3
    
    if arr[row][col] != 0:
        return solve(idx + 1)

    # 도미노를 채우려면 상하좌우 인접한 칸이 비어있어야 한다
    for x, y in dirs:
        
        new_row = row + x
        new_col = col + y
        new_box = (new_row // 3) * 3 + new_col // 3

        if 0 <= new_row < 9 and 0 <= new_col < 9 and arr[new_row][new_col] == 0:
            for num1 in range(1, 10):
                for num2 in range(1, 10):
                    if num1 == num2:
                        continue
                    # num1, num2 조합이 쓰일 수 있는지 확인
                    if domino[num1][num2]:
                        continue
                    if row_check[row][num1] or col_check[col][num1] or box_check[box][num1] or row_check[new_row][num2] or col_check[new_col][num2] or box_check[new_box][num2]:
                        continue
                    # 쓰일 수 있다면, 기록
                    # 도미노 기록
                    domino[num1][num2] = domino[num2][num1] = True
                    # 스도쿠 기록
                    arr[row][col] = num1
                    arr[new_row][new_col] = num2
                    # 체크용 기록
                    row_check[row][num1] = col_check[col][num1] = box_check[box][num1] = True
                    row_check[new_row][num2] = col_check[new_col][num2] = box_check[new_box][num2] = True
                    # 재귀함수 호출
                    if solve(idx + 1):
                        return True
                    # 백트래킹
                    domino[num1][num2] = domino[num2][num1] = False
                    arr[row][col] = 0
                    arr[new_row][new_col] = 0
                    row_check[row][num1] = col_check[col][num1] = box_check[box][num1] = False
                    row_check[new_row][num2] = col_check[new_col][num2] = box_check[new_box][num2] = False




puzzle = 1
while True:
    n = int(input())
    if n == 0:
        exit()
    
    arr = [[0] * 9 for _ in range(9)] # 스도쿠 판
    domino = [[False] * 10 for _ in range(10)] # domino[i][j] = domino[j][i] = 숫자 i, j 조합이 쓰였을 떄 True

    row_check = [[False] * 10 for _ in range(9)] # i행 숫자 j 존재 유무
    col_check =[[False] * 10 for _ in range(9)] # i열 숫자 j 존재 유무
    box_check = [[False] * 10 for _ in range(9)] # i번 박스 숫자 j 존재 유무

    for _ in range(n):
        u, lu, v, lv = input().split()
        ur, uc = to_row_col(lu)
        vr, vc = to_row_col(lv)
        u = int(u)
        v = int(v)
        # 도미노 기록
        domino[u][v] = domino[v][u] = True
        # 스도쿠 판에 숫자 기록
        arr[ur][uc] = u
        arr[vr][vc] = v
        # 존재 유무 기록
        row_check[ur][u] = True
        col_check[uc][u] = True
        box_check[(ur // 3) * 3 + uc // 3][u] = True
        row_check[vr][v] = True
        col_check[vc][v] = True
        box_check[(vr // 3) * 3 + vc // 3][v] = True
    
    # 채워져 있는 숫자 기록
    tmp = input().split()
    for i in range(9):
        r, c = to_row_col(tmp[i])
        # 스도쿠 판에 숫자 기록
        arr[r][c] = i + 1
        # 존재 유무 기록
        row_check[r][i + 1] = True
        col_check[c][i + 1] = True
        box_check[(r // 3) * 3 + c // 3][i + 1] = True

   
    print('Puzzle', puzzle)
    puzzle += 1
    solve(0)