import sys
input = sys.stdin.readline

N = int(input().strip())
# 입력받은 N*N 방을 벽(1)로 둘러싸게 (N+2)*(N+2) arr을 구성한다
arr = [[1]*(N+2)] + [[1] + list(map(int, input().split())) + [1]
                     for _ in range(N)] + [[1]*(N+2)]

# dp[r][c][0] = (r, c)까지 가로로 이동하는 방법의 수
# dp[r][c][1] = (r, c)까지 세로로 이동하는 방법의 수
# dp[r][c][2] = (r, c)까지 대각선으로 이동하는 방법의 수
dp = [[[0, 0, 0] for _ in range(N+2)] for __ in range(N+2)]

for r in range(1, N+1):
    for c in range(1, N+1):
        # 초기 파이프
        if (r, c) == (1, 2):
            dp[r][c] = [1, 0, 0]
            continue
        # 벽이면 skip
        if arr[r][c] == 1:
            continue
        # (r, c)까지 가로로 이동
        if 1 <= c-1 < N+1:
            dp[r][c][0] += dp[r][c-1][0]  # 이전 파이프 가로로 놓임
            dp[r][c][0] += dp[r][c-1][2]  # 이전 파이프 대각선으로 놓임
        # (r, c)까지 세로로 이동
        if 1 <= r-1 < N+1:
            dp[r][c][1] += dp[r-1][c][1]  # 이전 파이프 세로로 놓임
            dp[r][c][1] += dp[r-1][c][2]  # 이전 파이프 대각선으로 놓임
        # (r, c)까지 대각선으로 이동
        if 1 <= r-1 < N+1 and 1 <= c-1 < N+1:
            if arr[r][c-1] == 0 and arr[r-1][c] == 0:
                dp[r][c][2] += dp[r-1][c-1][0]  # 이전 파이프 가로로 놓임
                dp[r][c][2] += dp[r-1][c-1][1]  # 이전 파이프 세로로 놓임
                dp[r][c][2] += dp[r-1][c-1][2]  # 이전 파이프 대각선으로 놓임

"""
for row in dp:
    print(row)
"""
print(sum(dp[N][N]))
