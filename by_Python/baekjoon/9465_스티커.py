import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    # 스티커 점수 입력
    score = [[0]*(n+1)]
    score.append([0] + list(map(int, input().split())))
    score.append([0] + list(map(int, input().split())))

    # dp 배열
    dp = [[0] * (n+1) for __ in range(3)]

    for c in range(1, n+1):
        for r in range(1, 3):
            if r == 1:
                dp[1][c] = max(dp[2][c-1] + score[1][c], dp[1][c-1])
            else:  # r == 2
                dp[2][c] = max(dp[1][c-1] + score[2][c], dp[2][c-1])

    # 최대 점수 출력
    print(max(map(max, dp)))
