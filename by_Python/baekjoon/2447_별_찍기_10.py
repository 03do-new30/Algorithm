import sys
input = sys.stdin.readline

n = int(input())
arr = [[' '] * n for _ in range(n)]

def solve(n, r, c):
    if n == 3:
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if i == r + 1 and j == c + 1:
                    continue
                arr[i][j] = '*'
        return
    
    for i in range(r, r + n, n//3):
        for j in range(c, c + n, n//3):
            if i == r + n//3 and j == c + n//3:
                continue
            solve(n//3, i, j)

solve(n, 0, 0)
for row in arr:
    print(''.join(row))

