import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))

# dp[0][i] = 중간에 제거된 항 없이 +a[i]를 할 때 연속합 max
# dp[1][i] = 중간에 제거된 항 존재 +a[i]를 할 때 연속합 max

dp = [[0] * (n+1) for _ in range(2)]

for i in range(1, n+1):
    if i == 1:
        dp[0][i] = a[i]
        dp[1][i] = a[i]