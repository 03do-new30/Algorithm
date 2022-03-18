def solution(triangle):
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if (i, j) == 0:
                dp[i][j] = triangle[i][j]
                continue
            # 가장 왼쪽
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            # 가장 오른쪽
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            # 중간
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    answer = max(dp[n-1])
    return answer
