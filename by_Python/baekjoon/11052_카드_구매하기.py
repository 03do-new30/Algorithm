import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split(' ')))

# dp[i] = 카드 i개를 갖기 위해 지불해야 하는 금액의 최대값
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = p[i]
    for j in range(1, n+1):
        if i <= j:
            break
        dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[n])
