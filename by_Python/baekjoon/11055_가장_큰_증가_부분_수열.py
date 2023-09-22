import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))

# dp[i] = a[i]가 증가하는 부분 수열의 마지막 수일 때, 수열 합의 최대
# dp[i] = max(dp[j] (0 <= j < i and a[j] < a[i])) + a[i]
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += a[i]

print(max(dp))
