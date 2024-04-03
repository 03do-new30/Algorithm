import sys
from collections import deque
from itertools import product
sys.stdin = open("by_Python/SWEA/inputs/벽돌_깨기.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, col, row = map(int, input().split())
    # n개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거한다
    # 이때, 남은 벽돌의 개수
    arr = [[*map(int, input().split())] for _ in range(row)]

    # 남은 벽돌의 개수를 센다
    def count_bricks(arr):
        empty = 0
        for row_of_arr in arr:
            empty += row_of_arr.count(0)
        return row * col - empty
    
    def drop(arr, r, c):
        q = deque()
        visited = [[False] * col for _ in range(row)]
        q.append((r, c))
        visited[r][c] = True

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        while q:
            r, c = q.popleft()
            val = arr[r][c]
            # 폭발
            arr[r][c] = 0
            if val == 1:
                continue
            for i in range(4):
                for cnt in range(1, val):
                    nr = r + (dr[i] * cnt)
                    nc = c + (dc[i] * cnt)
                    if 0 <= nr < row and 0 <= nc < col:
                        if arr[nr][nc] > 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
    
    # 빈칸을 없앤다
    def update_arr(arr):
        for c in range(col):
            zeros = []
            not_zeros = []
            for r in range(row):
                if arr[r][c] == 0:
                    zeros.append(0)
                    continue
                not_zeros.append(arr[r][c])
            new_column = zeros + not_zeros
            for r in range(row):
                arr[r][c] = new_column[r]
    
    answer = float('inf')

    products = list(product([x for x in range(col)], repeat = n))
    
    for prod in products:
        tmp_arr = [row_of_arr[:] for row_of_arr in arr]
        
        for target_col in prod:
            
            columns = []
            for r in range(row):
                columns.append(arr[r][target_col])
            # 블럭이 존재하는가?
            if columns.count(0) == len(columns):
                break

            for r in range(row):
                if tmp_arr[r][target_col] == 0:
                    continue
                drop(tmp_arr, r, target_col)
                update_arr(tmp_arr)
                break

        left_bricks = count_bricks(tmp_arr)
        if left_bricks < answer:
            answer = left_bricks
        if left_bricks == 0:
            break
    
    print("#{0} {1}".format(test_case, answer))