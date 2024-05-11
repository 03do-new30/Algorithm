def solution(n, s, a, b, fares):
    # 인접행렬
    graph = [[0] * (n+1) for _ in range(n+1)]
    for fare in fares:
        u, v, price = fare
        graph[u][v] = price
        graph[v][u] = price
    
    INF = float('inf')

    # Dijkstra로도 풀 수 있음
    
    # Floyd-Warshall: 모든 지점에서 다른 모든 지점까지의 최단경로
    dp = [[0] * (n+1) for _ in range(n+1)]
    for u in range(1, n+1):
        for v in range(1, n+1):
            if u == v:
                dp[u][v] = 0
                continue
            if graph[u][v] > 0:
                dp[u][v] = graph[u][v]
            else:
                dp[u][v] = INF
    # 정점 x를 거쳐갈 때를 기준으로 판단
    for mid_node in range(1, n+1):
        for u in range(1, n+1):
            for v in range(1, n+1):
                if u == mid_node or v == mid_node:
                    continue
                if dp[u][v] == 0:
                    continue
                dp[u][v] = min(dp[u][v], dp[u][mid_node] + dp[mid_node][v])
    
    # 최솟값을 찾아주면 된다
    # dp[i][j] = i번 지점에서 j번 지점까지 갈 때의 최저 택시요금
    # answer = min(dp[s][k] + dp[k][a] + dp[k][b])
    answer = INF
    for k in range(1, n+1):
        if answer > dp[s][k] + dp[k][a] + dp[k][b]:
            answer = dp[s][k] + dp[k][a] + dp[k][b]
    return answer

n = [6, 7, 6]
s = [4, 3, 4]
a = [6, 4, 5]
b = [2, 1, 6]
fares = [[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]]
result = [82, 14, 18]

for i in range(len(result)):
    print(solution(n[i], s[i], a[i], b[i], fares[i]) == result[i])
    print('-' * 30)