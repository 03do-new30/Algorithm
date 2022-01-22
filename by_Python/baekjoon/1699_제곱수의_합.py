import sys
import math
input = sys.stdin.readline

n = int(input().strip())

dp = [0]*(n+1)

# bottom-up 방식


def bottom_up(n):
    # 제곱수는 1로 초기화
    x = 1
    while x*x <= n:
        dp[x*x] = 1
        x += 1

    # n의 값이 0이 아니면(제곱수) 리턴
    if dp[n] != 0:
        return dp[n]

    for i in range(1, n+1):
        if dp[i] != 0:
            continue

        mini = i
        # j*j <= i인 것 중
        # dp[j*j] + dp[i-j*j]의 값이 최소인 것을
        # dp[i]의 값으로 갱신
        for j in range(1, int(math.sqrt(i)) + 1):
            if 1 + dp[i-j*j] < mini:
                mini = 1 + dp[i-j*j]  # 1 = dp[j*j]
        dp[i] = mini

    return dp[n]


print(bottom_up(n))
