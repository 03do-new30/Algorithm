import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

str1 = " " + input().strip()
str2 = " " + input().strip()

dp = [[0]*len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


def dfs(r, c, LCS_str):
    # return
    if dp[r][c] == 0:
        return LCS_str

    move_r = [0, -1, -1]
    move_c = [-1, 0, - 1]

    for i in range(3):
        new_r = r + move_r[i]
        new_c = c + move_c[i]
        if 0 <= new_r < len(str1) and 0 <= new_c < len(str2):
            # 왼쪽, 위쪽으로 이동하는 경우는 dp[r][c]와 dp[new_r][new_c]가 같을 때
            if i == 0 or i == 1:
                if dp[new_r][new_c] == dp[r][c]:
                    return dfs(new_r, new_c, LCS_str)
            # 왼쪽 대각선 위로 이동하는 경우는 dp[new_r][new_c]가 dp[r][c]-1일 때
            else:
                if dp[new_r][new_c] == dp[r][c] - 1:
                    return dfs(new_r, new_c, str1[r] + LCS_str)


# LCS의 길이
LCS_len = dp[len(str1) - 1][len(str2) - 1]
print(LCS_len)
if LCS_len > 0:
    # backward path로 LCS 찾기
    i = len(str1) - 1
    j = len(str2) - 1
    LCS_str = dfs(i, j, "")
    print(LCS_str)
