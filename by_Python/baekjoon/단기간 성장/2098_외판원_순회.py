import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

# dp[city][history] = 현재 위치가 city이고, 방문 기록이 history일 때, **이 시점에서 다시 출발점인 0까지 순회할 때**의 최소 비용을 저장한다.
# 방문 기록 = 비트마스크
dp = [[0] * ((1 << n)) for _ in range(n)]

INF = float('inf')

def dfs(city, history):
    # 최소 비용이 존재할 때
    if dp[city][history] > 0:
        return dp[city][history]

    # 모든 경로를 방문했을 때
    if history == (1 << n) - 1:
        # 다시 출발 도시 0으로 돌아갈 수 없는 경우
        if not w[city][0]:
            return INF
        # 현재 위치에서 출발 도시 0으로 돌아가는 경우의 비용을 반환
        return w[city][0]
    
    # 다음 방문 도시 결정
    min_cost = INF
    for next_city in range(n):
        # 경로가 없는 경우
        if not w[city][next_city]:
            continue
        # 이미 방문한 경우
        if (1 << next_city & history) > 0 :
            continue
        # 방문할 수 있는 도시인 경우
        # 현재 위치에서 next_city까지의 이동 비용 + next_city에서 출발점 0으로 돌아가는 이동 비용 합산
        current_cost = w[city][next_city] + dfs(next_city, 1 << next_city | history)
        min_cost = min(min_cost, current_cost)
    
    dp[city][history] = min_cost
    return min_cost

ans = dfs(0, 1)
for row in dp:
    print(row)
print(ans)