import sys
input = sys.stdin.readline

n = int(input())
row = []
col = []
for _ in range(n):
    r, c = map(int, input().split())
    row.append(r)
    col.append(c)

# dp[i][j] = 행렬 i ~ 행렬 j를 곱셈할 때, 곱셈 횟수의 최소값
# dp[i][j] = min{ 
#     dp[i][k] + dp[k+1][j] + row[i] * col[k] * col[j] 
#     } for (i <= k < j)

dp = [[-1] * n for _ in range(n)]

for x in range(n):
    for i in range(n):
        j = i + x
        
        if j >= n:
            break

        if i == j:
            dp[i][j] = 0
        else:
            tmp = []
            for k in range(i, j):
                tmp.append(dp[i][k] + dp[k+1][j] + row[i] * col[k] * col[j])
            dp[i][j] = min(tmp)

print(dp[0][n-1])