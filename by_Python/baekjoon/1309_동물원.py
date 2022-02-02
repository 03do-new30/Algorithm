import sys
input = sys.stdin.readline

n = int(input().strip())

# dp[n][0] = n번째 줄에 사자가 없음
# dp[n][1] = n번째 줄의 왼쪽에 사자 배치
# dp[n][2] = n번째 줄의 오른쪽에 사자 배치
dp = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 1
    else:
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
        dp[i][1] = dp[i-1][0] + dp[i-1][2] % 9901
        dp[i][2] = dp[i-1][0] + dp[i-1][1] % 9901

# dp[n]의 합이 9901을 초과할 수 있으므로 마지막에 한 번 더 연산!!!
print(sum(dp[n]) % 9901)
