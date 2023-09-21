import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    # 스티커 점수 입력
    score = [[0]*(n+1)]
    score.append([0] + list(map(int, input().split())))
    score.append([0] + list(map(int, input().split())))

    dp = [[0] * (n+1) for _ in range(3)]
    for i in range(1, n+1):
        if i -2 >= 0:
            dp[1][i] = max(dp[1][i-2], dp[2][i-2])
            dp[2][i] = max(dp[1][i-2], dp[2][i-2])
        if i - 1 >= 0:
            dp[1][i] = max(dp[1][i], dp[2][i-1])
            dp[2][i] = max(dp[2][i], dp[1][i-1])
        dp[1][i] += score[1][i]
        dp[2][i] += score[2][i]
        
    
    print(max(map(max, dp)))