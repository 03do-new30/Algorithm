import sys
input = sys.stdin.readline

n = int(input())
arr = [[' '] * (2*n) for _ in range(n)]


def draw_from_top(r, c):
    arr[r][c] = '*'

    for j in range(c-1, c+2):
        if j == c:
            continue
        arr[r+1][j] = '*'
    
    for j in range(c-2, c+3):
        arr[r+2][j] = '*'

def solve(n, r, c):
    if n == 3:
        draw_from_top(r, c)
        return
    
    solve(n//2, r, c)
    solve(n//2, r + n//2, c - n//2)
    solve(n//2, r + n//2, c + n//2)

solve(n, 0, n-1)

for row in arr:
    print(''.join(row))