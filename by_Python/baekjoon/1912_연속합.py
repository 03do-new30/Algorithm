import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# dp[i] = arr[i]를 마지막으로 더할 때 연속된 수의 합의 최대
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = arr[i]
        continue

    dp[i]  = max(arr[i], dp[i-1] + arr[i])

print(max(dp))