import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]


### 1 ###
# 모두 같은색으로 이루어진 가장 긴 연속 부분 찾기
def count_candy():
    ret = 0
    # 행 검사
    for r in range(n):
        row_cnt = 0
        for c in range(n):
            if c == 0:
                row_cnt = 1
                continue
            if arr[r][c] == arr[r][c-1]:
                row_cnt += 1
            else:
                ret = max(ret, row_cnt)
                row_cnt = 1
        ret = max(ret, row_cnt)
    # 열 검사
    for c in range(n):
        col_cnt = 0
        for r in range(n):
            if r == 0:
                col_cnt = 1
                continue
            if arr[r][c] == arr[r-1][c]:
                col_cnt += 1
            else:
                ret = max(ret, col_cnt)
                col_cnt = 1
        ret = max(ret, col_cnt)
    
    return ret
            
### 2 ###
# 인접한 칸 -> 각 칸의 우측 & 하단만 검사해줘도 가능
dirs = [(0, 1), (1, 0)]

### 3 ###
max_candy = 0
for r in range(n):
    for c in range(n):
        for x, y in dirs:
            new_r = r + x
            new_c = c + y
            if 0 <= new_r < n and 0 <= new_c < n:
                if arr[r][c] != arr[new_r][new_c]:
                    # swap
                    arr[r][c], arr[new_r][new_c] = arr[new_r][new_c], arr[r][c]
                    # count
                    max_candy = max(max_candy, count_candy())
                    # re-swap
                    arr[r][c], arr[new_r][new_c] = arr[new_r][new_c], arr[r][c]

print(max_candy)