import sys
input = sys.stdin.readline

t = int(input())
cases = [int(input()) for _ in range(t)]
max_case = max(cases)

dp = [0] * (max_case + 1)
mod = 1000000009

dp[0] = 1
for i in range(1, max_case + 1):
    if i - 1 >= 0:
        dp[i] += dp[i-1]
    if i - 2 >= 0:
        dp[i] += dp[i-2]
    if i - 3 >= 0:
        dp[i] += dp[i-3]
    dp[i] %= mod

for case in cases:
    print(dp[case])
