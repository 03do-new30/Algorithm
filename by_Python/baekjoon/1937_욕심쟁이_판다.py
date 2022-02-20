import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

# dp[r][c] = (r, c)에서 갈 수 있는 최대 칸 수
# 방문하지 않았을 때는 0으로 초기화
dp = [[0]*n for _ in range(n)]


def dfs(r, c):
    # 방문 기록이 있으면 return
    if dp[r][c] != 0:
        return dp[r][c]

    # 방문 기록이 없으면 1
    if dp[r][c] == 0:
        dp[r][c] = 1

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if arr[r][c] < arr[nr][nc]:
                dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)

    return dp[r][c]


ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans, dfs(r, c))

print(max(map(max, dp)))
