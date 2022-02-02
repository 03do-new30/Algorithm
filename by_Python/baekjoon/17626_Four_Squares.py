import math
import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0]*(n+1)
# 제곱수에는 1을 미리 표시
k = 1
while k*k <= n:
    dp[k*k] = 1
    k += 1

for i in range(1, n+1):
    # i가 제곱수이면 skip
    if dp[i] == 1:
        continue

    min_value = 10**6
    j = 1
    while j*j <= i:
        min_value = min(min_value, dp[i-j*j] + 1)
        j += 1
    dp[i] = min_value

print(dp[n])
