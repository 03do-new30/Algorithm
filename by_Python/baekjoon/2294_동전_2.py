import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input().strip()))
dp = [-1]*(1000001)

# dp 초기화
# dp[x] = x원을 만들기 위해 사용한 동전의 최소 개수
dp[0] = 0
for coin in coins:
    # 가치가 같은 동전이 여러 번 주어질 수 있다.
    # 이미 dp[coin] = 1 이라면 그냥 스킵
    if dp[coin] == -1:
        dp[coin] = 1


for i in range(1, k+1):
    #print("i", i, "->", dp)
    if dp[i] != -1:
        continue

    tmp = []
    for coin in coins:
        if i - coin >= 0 and dp[i-coin] != -1:
            tmp.append(dp[coin] + dp[i-coin])

    if len(tmp) <= 0:
        continue
    dp[i] = min(tmp)

print(dp[k])
