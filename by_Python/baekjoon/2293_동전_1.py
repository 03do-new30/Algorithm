import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().strip()) for _ in range(n)]

dp = [1] + [0]*k  # dp[0] = 1

for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]
    """
    print(coin, "원짜리 동전까지를 사용했을 때")
    print(dp)
    print("-"*10)
    """

print(dp[k])
