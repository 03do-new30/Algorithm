import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split(' ')))

# dp[i] = 수열의 마지막 숫자가 a[i]일 때, 증가하는 부분 수열의 길이
# dp[i] = max(dp[j] (0 <= j < i and a[j] < a[i]인 항에 대해) ) + 1
dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1 
print(max(dp))