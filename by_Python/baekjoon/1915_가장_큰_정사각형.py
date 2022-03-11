# https://kyun2da.github.io/2021/04/09/biggestSquare/
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
"""
for row in arr:
    print(row)
"""

# dp[r][c] = 어떤 정사각형의 우측 하단 꼭짓점이 (r, c)일 때, 그 정사각형의 최대 변의 길이가 될 수 있는 값
dp = [[0]*m for _ in range(n)]

for r in range(n):
    for c in range(m):
        if r == 0 or c == 0:
            dp[r][c] = arr[r][c]

        elif arr[r][c] == 0:
            dp[r][c] = 0

        else:  # arr[r][c] == 1
            dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1

"""
print('-'*30)
for row in dp:
    print(row)
"""

ans = max(map(max, dp))
print(ans**2)
