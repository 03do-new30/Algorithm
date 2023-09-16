import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split(' ')))

# dp[i] = 민규가 카드 i개를 갖기 위해 지불해야하는 금액 최솟값
dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1:
            dp[i] = dp[i-j] + p[j]
        else:
            dp[i] = min(dp[i], dp[i-j] + p[j])
print(dp[n])