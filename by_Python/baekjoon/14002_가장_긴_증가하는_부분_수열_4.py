import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))

# dp[i] = a[i]가 마지막 수일 때 LIS의 길이
# seq[i] = a[i]가 마지막 수일 때, 그때까지의 LIS 수열 기록
dp = [0] * (n+1)
seq = [[] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            seq[i] = seq[j] + [a[i]]

ans_len = 0
ans_seq = []
for i in range(1, n+1):
    if dp[i] > ans_len:
        ans_len = dp[i]
        ans_seq = seq[i]

print(ans_len)
print(' '.join(map(str, ans_seq)))