import sys
input = sys.stdin.readline

# 참고: https://shoark7.github.io/programming/algorithm/solve-tsp-with-dynamic-programming

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
VISITED_ALL = (1 << N) - 1 # 2^N - 1
INF = float('inf')
dp = [[INF]*(1<<N) for _ in range(N)] #row = 도시의 개수, col = 방문 여부 비트로 표시

def find_path(last, visited):
    # 모든 도시 방문
    if visited == VISITED_ALL:
        # 출발점으로 가는 경로가 있음
        if W[last][0]:
            return W[last][0]
        else:
            return INF
    
    # 이미 최소 비용이 계산되어 있다면
    if dp[last][visited] != INF:
        return dp[last][visited]
    
    # 모든 도시를 탐방
    for i in range(1, N):
        if not W[last][i]: # 가는 경로가 없으면 스킵
            continue
        if visited & (1<<i): # 이미 방문한 도시라면 스킵
            continue
        # 점화식 부분
        dp[last][visited] = min(dp[last][visited], find_path(i, visited | (1<<i)) + W[last][i])

    return dp[last][visited]

print(find_path(0, 1))
