import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# dp[r][c] = (r, c)에서 (m-1, n-1)까지 갈 수 있는 경로의 수
# 방문하지 않았을 때는 -1로 초기화
# 시간초과를 피하기 위해 DP + DFS 전략
dp = [[-1] * n for _ in range(m)]


def dfs(r, c):
    # 도착점에서 도착점으로 갈 수 있는 경로의 수는 1
    if r == m-1 and c == n-1:
        dp[r][c] = 1

    # 방문 기록이 있으면 return
    if dp[r][c] != -1:
        return dp[r][c]

    # 아직 방문하지 않음 -> 0으로 업데이트
    if dp[r][c] == -1:
        dp[r][c] = 0

    for i in range(4):
        new_r = r + dx[i]
        new_c = c + dy[i]
        if 0 <= new_r < m and 0 <= new_c < n:
            if board[new_r][new_c] < board[r][c]:
                dp[r][c] += dfs(new_r, new_c)

    return dp[r][c]


print(dfs(0, 0))
# print(dp)
