import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0] + list(map(int, input().split()))

# s~e까지의 숫자가 팰린드롬인지 확인하는 방법
# s번째 숫자 == e번째 숫자이고, s+1 ~ e-1의 숫자가 팰린드롬이면 팰린드롬
dp = [[1]*(N+1) for _ in range(N+1)]

# 초기화
# 구간: 1
for i in range(1, N+1):
    dp[i][i] = 1

# 구간: 2
for i in range(1, N+1):
    for j in range(i, N+1):
        if i + 1 == j:
            if arr[i] == arr[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

# 구간: 3 이상
for x in range(2, N):
    for i in range(1, N+1):
        if i + x <= N:
            j = i + x
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 0

M = int(input().strip())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s][e])
