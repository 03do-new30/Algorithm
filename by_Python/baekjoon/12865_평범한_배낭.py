import sys
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())
W = [0]
V = [0]
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# dp 초기화
dp = [[0] * (K+1) for _ in range(N + 1)]

# dp[i][wt]:
# i번째 물건까지 가방에 넣을 수 있는 경우,
# 가방 무게가 wt라면 이 때의 가치합의 최대

for i in range(1, N+1):
    for wt in range(1, K+1):
        if wt < W[i]:
            dp[i][wt] = dp[i-1][wt]
        else:
            dp[i][wt] = max(dp[i-1][wt-W[i]] + V[i], dp[i-1][wt])


print(max(map(max, dp)))
