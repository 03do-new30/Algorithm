import sys
input = sys.stdin.readline

n = int(input())

# dp[i][j] = 길이가 i이고, 끝자리가 j로 끝나는 수의 개수
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
#            (단 j-1 >= 0,  j+1 < 10)
dp = [[0] * 10 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(0, 10):
        
        if i == 1:
            if j != 0:
                dp[i][j] = 1
        
        else:
            if j - 1 >= 0:
                dp[i][j] += dp[i-1][j-1]
            if j + 1 < 10:
                dp[i][j] += dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)