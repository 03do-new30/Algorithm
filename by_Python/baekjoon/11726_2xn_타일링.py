import sys
input = sys.stdin.readline

n = int(input())

# dp[i] = 2 * i 직사각형을 채우는 방법의 수
dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
        continue
    if i == 2:
        dp[i] = 2
        continue

    dp[i] = (dp[i-2] + dp[i-1]) % 10007

print(dp[n])