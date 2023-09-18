import sys
import math
input = sys.stdin.readline

n = int(input())

# dp[i] = i를 제곱수의 합으로 표현할 때 항의 최소 개수
dp = [0] * (n+1)
squares = [] # 제곱수들을 저장한다

# dp[i] = 1 (i가 제곱수일 경우)
for i in range(1, n + 1):
    
    dp[i] = i
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        j += 1
print(dp[n])
 