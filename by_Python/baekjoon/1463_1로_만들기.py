import sys
input = sys.stdin.readline

n = int(input())

# dp[x] = x를 1로 만드는 연산 횟수 최소값
# dp[x] = min(dp[x//2] + 1, -> when x % 2 == 0 
#             dp[x//3] + 1, -> when x % 3 == 0 
#             dp[x-1] + 1 )

dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        continue
    
    cnt = dp[i-1] + 1

    if i % 2 == 0:
        cnt = min(cnt, dp[i//2] + 1)
    if i % 3 == 0:
        cnt = min(cnt, dp[i//3] + 1)
    
    dp[i] = cnt

print(dp[n])