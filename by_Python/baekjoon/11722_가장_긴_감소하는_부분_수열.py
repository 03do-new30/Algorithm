import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))

# 수열 a를 뒤집어서 가장 긴 증가하는 부분 수열을 구한다
a.reverse()

# dp[i] = a[i]가 수열의 마지막 수일 때, 가장 긴 증가하는 부분 수열의 길이
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = 1
        continue
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(max(dp))