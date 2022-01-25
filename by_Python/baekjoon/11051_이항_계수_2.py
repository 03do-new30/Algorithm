import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 파스칼의 삼각형 이용
#dp[n][k] = nCk
dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(0, n+1):
        if j == 0 or j == i:
            dp[i][j] = 1
            continue
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
for row in dp:
    print(row)
print(dp[n][k])
