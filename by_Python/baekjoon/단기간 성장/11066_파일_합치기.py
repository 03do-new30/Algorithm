import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    chapters = [0] + list(map(int, input().split()))
    
    # cost[i] = chapter 1 ~ chapter i 까지 파일 크기의 누적합
    cost = [0] * (K + 1)
    for i in range(K + 1):
        if i == 0:
            continue
        cost[i] = cost[i-1] + chapters[i]
    
    # dp[i][j] = chapter i ~ chapter j 까지 파일을 합칠 때 최소 비용
    # dp[i][j] = for i <= k < j, 
    #            min(dp[i][k] + dp[k+1][j]) + cost[j] - cost[i-1]
    
    # ↘️ 대각선 방향으로 순회한다
    dp = [[0] * (K + 1) for _ in range(K + 1)]
    for x in range(K):
        for i in range(1, K+1):
            j = i + x
            if j >= K + 1:
                break
            
            # 자기 자신을 합치는 비용은 0이다.
            if i == j:
                continue

            # 연속된 두 챕터를 합치는 비용
            if j == i + 1:
                dp[i][j] = chapters[i] + chapters[j]
                continue
            
            memo = []
            for m in range(i, j):
                memo.append(dp[i][m] + dp[m+1][j])
            dp[i][j] = min(memo) + cost[j] - cost[i-1]

    print(dp[1][K])