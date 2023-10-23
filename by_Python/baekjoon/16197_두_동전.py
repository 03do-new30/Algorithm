import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 동전 위치 기록
coins = []
for r in range(n):
    for c in range(m):
        if len(coins) == 2:
            break
        if arr[r][c] == 'o':
            arr[r][c] = '.'
            coins.append((r, c))

def solve(ar, ac, br, bc, count):

    if count == 11:
        return -1

    a_drop = True
    b_drop = True
    if 0 <= ar < n and 0 <= ac < m:
        a_drop = False
    if 0 <= br < n and 0 <= bc < m:
        b_drop = False
    
    # 동전이 둘 다 떨어진 경우
    if a_drop and b_drop:
        return -1
    # 동전이 하나만 떨어진 경우
    elif a_drop or b_drop:
        return count
    
    ret = -1

    for x, y in dirs:
        new_ar = ar + x
        new_ac = ac + y
        new_br = br + x
        new_bc = bc + y

        if 0 <= new_ar < n and 0 <= new_ac < m:
            if arr[new_ar][new_ac] == '#':
                new_ar = ar
                new_ac = ac
        
        if 0 <= new_br < n and 0 <= new_bc < m:
            if arr[new_br][new_bc] == '#':
                new_br = br
                new_bc = bc

        tmp = solve(new_ar, new_ac, new_br, new_bc, count + 1)
        if tmp == -1:
            continue
        if ret == -1 or ret > tmp:
            ret = tmp
    
    return ret

ar, ac = coins[0]
br, bc = coins[1]
answer = solve(ar, ac, br, bc, 0)
print(answer)