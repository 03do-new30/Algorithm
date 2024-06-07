import sys
input = sys.stdin.readline

n, k = map(int, input().split())

items = [(0, 0)]
for _ in range(n):
    wt, val = map(int, input().split())
    items.append((wt, val))

# dp[i][j] = i번째 물건을 넣어서 배낭 무게의 합이 총 j가 될 때, 가치의 합
dp = [[0] * (k + 1) for _ in range(n+1)]
for i in range(1, n+1):
    i_wt, i_val = items[i]
    for wt in range(1, k+1):
        if wt < i_wt:
            dp[i][wt] = dp[i-1][wt]
        else:
            dp[i][wt] = max(dp[i-1][wt - i_wt] + i_val, dp[i-1][wt])

print(max(map(max, dp)))