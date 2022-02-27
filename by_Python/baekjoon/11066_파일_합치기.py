import sys
input = sys.stdin.readline


for _ in range(int(input().strip())):
    k = int(input().strip())
    arr = [0] + list(map(int, input().split()))

    # sums[i] = 1~i까지의 파일 크기 합
    sums = [0]*(k+1)
    for i in range(1, k+1):
        sums[i] = sums[i-1] + arr[i]

    # dp[i][j] = 파일 i ~ j까지 합칠 때 필요한 최소비용
    dp = [[-1]*(k+1) for _ in range(k+1)]

    # 초기화
    for i in range(1, k+1):
        dp[i][i] = 0

    # 대각선방향↘ 으로 순회할 수 있게 함
    # 1, 2 -> 2, 3 -> 3, 4 -> 1, 3 -> 2, 4 -> ...
    for i in range(1, k+1):
        for start in range(1, k+1):
            end = start + i
            if end > k:
                continue

            min_cost = 10**9
            for mid in range(start, end):
                min_cost = min(min_cost, dp[start][mid] + dp[mid+1][end])
            dp[start][end] = min_cost + sums[end] - sums[start-1]

    print(dp[1][k])


""" topdown (시간초과)
def solve(start, end):
    if start == end:
        dp[start][end] = 0
        return 0

    if start + 1 == end:
        dp[start][end] = arr[start] + arr[end]
        return dp[start][end]

    min_cost = 10**9
    for mid in range(start, end):
        min_cost = min(min_cost, solve(start, mid) + solve(mid+1, end))
    dp[start][end] = min_cost + sums[end] - sums[start-1]
    return dp[start][end]


for _ in range(int(input().strip())):
    k = int(input().strip())
    arr = [0] + list(map(int, input().split()))

    # sums[i] = 1~i까지의 파일 크기 합
    sums = [0]*(k+1)
    for i in range(1, k+1):
        sums[i] = sums[i-1] + arr[i]

    dp = [[-1]*(k+1) for _ in range(k+1)]

    print(solve(1, k))
"""
