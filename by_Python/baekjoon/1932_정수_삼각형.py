import sys
input = sys.stdin.readline

n = int(input())

### 1 ###
# 삼각형 저장
arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    nums = [0] + list(map(int, input().split()))
    for j in range(1, i+1):
        arr[i][j] = nums[j]

### 2 ###
# dp[i][j] = arr[i][j] 위치를 더할 때, 최대값
# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[n]))
