import sys
input = sys.stdin.readline

k = int(input().strip())
dp = [(-1, -1) for _ in range(k+1)]
dp[0] = (1, 0)

# 모든 B는 BA로 바뀌고, A는 B로 바뀐다
# (0, 1), (1, 1), (1, 2), (2, 3)


def button(n):
    prev_a = dp[n-1][0]
    prev_b = dp[n-1][1]
    dp[n] = (prev_b, prev_a + prev_b)


for i in range(1, k + 1):
    button(i)

print(dp[k][0], dp[k][1])
