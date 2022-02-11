import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp[r][c] = (r, c)까지의 경로의 수
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        if r == N-1 and c == N-1:
            print(dp[r][c])
            break

        # 칸에 쓰여있는 숫자
        number = arr[r][c]

        if r + number < N:
            dp[r+number][c] += dp[r][c]
        if c + number < N:
            dp[r][c+number] += dp[r][c]

""" 이렇게 풀수도 있음 (백준 1520 내리막길 풀이과정 활용)

# dp[r][c] = (r, c)에서 (N-1, N-1)-도착점-까지 갈 수 있는 경로의 수
# 방문하지 않았을 때는 -1로 초기화
# 시간 초과를 피하기 위해 DP + DFS 전략
dp = [[-1]*N for _ in range(N)]


def dfs(r, c):
    # 도착점에서 도착점으로 가는 경로는 1
    if r == N-1 and c == N-1:
        dp[r][c] = 1

    # 방문 기록이 있으면 return
    if dp[r][c] != -1:
        return dp[r][c]

    # 아직 방문하지 않았다면 0으로 업데이트
    if dp[r][c] == -1:
        dp[r][c] = 0

    # 칸에 써있는 숫자
    number = arr[r][c]

    if 0 <= r + number < N:
        dp[r][c] += dfs(r+number, c)

    if 0 <= c + number < N:
        dp[r][c] += dfs(r, c+number)

    return dp[r][c]


print(dfs(0, 0))
"""
