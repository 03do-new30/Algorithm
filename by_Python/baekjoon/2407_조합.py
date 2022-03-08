import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if j == 1:
            dp[i][j] = i
        elif j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[n][m])

# dp[n][m] = nCm
# dp[n][1] = n, dp[n][n] = 1
# dp[n][m] = dp[n-1][m] + dp[n-1][m-1]
"""
0  1  2  3  4  5
-----------------
1 |1   
  |
2 |2  1
  |
3 |3  3  1
  |
4 |4  6  4  1
  |
5 |5  10 10 5  1
"""
