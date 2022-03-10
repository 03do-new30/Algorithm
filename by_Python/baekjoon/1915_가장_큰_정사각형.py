# https://kyun2da.github.io/2021/04/09/biggestSquare/
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*(m+1)] + [[0] + list(map(int, list(input().strip())))
                     for _ in range(n)]
"""
for row in arr:
    print(row)
"""

# dp[r][c] = 우측 하단 꼭짓점이 (r,c)인 영역 내의 정사각형의 최대 변의 길이
# 정사각형이 될 수 없을 때는 0으로 표시
dp = [[0]*(m+1) for _ in range(n+1)]

for r in range(1, n+1):
    for c in range(1, m+1):
        if r == 1 or c == 1:
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
