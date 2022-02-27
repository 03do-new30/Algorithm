import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

max_dp = [arr[0][0], arr[0][1], arr[0][2]]
min_dp = [arr[0][0], arr[0][1], arr[0][2]]

for i in range(1, N):
    zero, one, two = map(int, max_dp)
    max_dp[0] = arr[i][0] + max(zero, one)
    max_dp[1] = arr[i][1] + max(zero, one, two)
    max_dp[2] = arr[i][2] + max(one, two)

    zero, one, two = map(int, min_dp)
    min_dp[0] = arr[i][0] + min(zero, one)
    min_dp[1] = arr[i][1] + min(zero, one, two)
    min_dp[2] = arr[i][2] + min(one, two)

print(max(max_dp), min(min_dp))
