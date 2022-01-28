import sys
input = sys.stdin.readline

n, m = map(int, input().split())
candy = [[0]*(m+2)] + [[0] + list(map(int, input().split())) + [0]
                       for _ in range(n)] + [[0]*(m+2)]

"""
print("candy")
for row in candy:
    print(row)
"""

# dp[r][c] = (r, c)로 이동할 때 가져올 수 있는 사탕 개수의 최대값
dp = [[0]*(m+2)] + [[0]*(m+2) for _ in range(n)] + [[0]*(m+2)]
for r in range(1, n+1):
    for c in range(1, m+1):
        dp[r][c] = max(dp[r][c], dp[r-1][c] + candy[r][c], dp[r]
                       [c-1] + candy[r][c], dp[r-1][c-1] + candy[r][c])

"""
print("dp")
for row in dp:
    print(row)
"""

print(dp[n][m])
