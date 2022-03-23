import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(tuple(map(int, input().split())))

# dp[i][j] = 행렬 i~j까지 곱했을 때, 곱셈 연산 횟수의 최솟값
dp = [[0]*N for _ in range(N)]
# 대각선↘︎으로 순회하며 값 채우기
for idx in range(1, N):
    for i in range(N):
        j = i + idx
        if j < N:
            if j == i+1:
                dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            else:
                dp[i][j] = 2**31 - 1
                
                # (i~x) * (x~j)
                # A(BCD) | (AB)(CD) | (ABC)D
                for x in range(i, j+1):
                    if x == i:
                        dp[i][j] = min(dp[i][j], 
                        dp[i+1][j] + matrix[i][0]*matrix[i+1][0]*matrix[j][1])
                    elif x == j:
                        dp[i][j] = min(dp[i][j], 
                        dp[i][j-1] + matrix[i][0]*matrix[j][0]*matrix[j][1])
                    else:
                        dp[i][j] = min(dp[i][j],
                        dp[i][x] + dp[x+1][j] + matrix[i][0]*matrix[x+1][0]*matrix[j][1])

print(dp[0][N-1])