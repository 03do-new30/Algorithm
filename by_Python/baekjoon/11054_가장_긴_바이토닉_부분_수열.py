import sys
input = sys.stdin.readline

n = int(input().strip())
a = [0] + list(map(int, input().split()))

# dp[i] = a[i]가 바이토닉 수열의 기준점일 때, 가장 긴 수열의 길이
# LIS[i] = a[i]가 마지막일 때, 가장 긴 증가하는 수열의 길이
# LDS[i] = a[i]가 시작점일 때, 가장 긴 감소하는 수열의 길이
# dp[i] = LIS[i] + LDS[i] - 1
dp = [0] * (n+1)
LIS = [0] * (n+1)
LDS = [0] * (n+1)

# LIS
for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            LIS[i] = max(LIS[i], LIS[j])
    LIS[i] += 1
# LDS
for i in range(n, -1, -1):
    for j in range(n, i, -1):
        if a[j] < a[i]:
            LDS[i] = max(LDS[i], LDS[j])
    LDS[i] += 1


for i in range(1, n+1):
    dp[i] = LIS[i] + LDS[i] - 1

print(max(dp))