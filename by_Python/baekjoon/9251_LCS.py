import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        # 같은 문자일 때
        if s1[i-1] == s2[j-1]:
            # 지금까지의 LCS + 1
            dp[i][j] = dp[i-1][j-1] + 1
        # 다른 문자일 때
        else:
            # 이전 검사까지 중 가장 컸던 값으로 유지
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(map(max, dp)))
