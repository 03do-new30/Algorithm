import sys
input = sys.stdin.readline

t = int(input())
nums = []
n = 0
for _ in range(t):
    x = int(input())
    n = max(n, x)
    nums.append(x)

# dp[r][n] = 마지막에 r을 더해서 정수 n을 나타내는 방법의 수 (1 <= r <= 3)
# dp[0][n] = n을 1, 2, 3의 합으로 나타내는 방법의 수 (단, 같은 수를 두번 이상 연속해서 사용하지 않음)
# dp[0][n] = dp[1][n] + dp[2][n] + dp[3][n]
#          = (dp[2][n-1] + dp[3][n-1]) +
#            (dp[1][n-2] + dp[3][n-2]) +
#            (dp[1][n-3] + dp[2][n-3])
dp = [[0] * (n+1) for _ in range(4)]

for i in range(1, n+1):
    if i >= 1:
        dp[1][i] = dp[2][i-1] + dp[3][i-1]
        if i == 1:
            dp[1][i] += 1
    if i >= 2:
        dp[2][i] = dp[1][i-2] + dp[3][i-2]
        if i == 2:
            dp[2][i] += 1
    if i >= 3:
        dp[3][i] = dp[1][i-3] + dp[2][i-3]
        if i == 3:
            dp[3][i] += 1
    
    dp[1][i] = dp[1][i] % 1000000009
    dp[2][i] = dp[2][i] % 1000000009
    dp[3][i] = dp[3][i] % 1000000009

for num in nums:
    dp[0][num] = (dp[1][num] + dp[2][num] + dp[3][num]) % 1000000009
    print(dp[0][num])