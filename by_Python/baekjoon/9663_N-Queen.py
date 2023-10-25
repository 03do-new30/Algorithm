import sys
input = sys.stdin.readline

n = int(input())
ans = 0

col_check = [False] * n
diag_check_1 = [False] * (2*n-1)
diag_check_2 = [False] * (2*n-1)

def solve(row):
    global ans, col_check, diag_check_1, diag_check_2

    if row == n:
        ans += 1
        return
    
    for col in range(n):
        if not(col_check[col] or diag_check_1[row + col] or diag_check_2[row - col + n - 1]):
            col_check[col] = diag_check_1[row + col] = diag_check_2[row - col + n - 1] = True
            solve(row + 1)
            col_check[col] = diag_check_1[row + col] = diag_check_2[row - col + n - 1] = False

solve(0)
print(ans)