import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

# n*n 배열의 누적합을 구한다
# prefix_sum[i][j] = (1, 1)  ~ (i, j) 까지의 누적합
prefix_sum = [[0] * (n+1) for _ in range(n+1)]
# 먼저, 가로로 구간 합을 구해준다
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + arr[i][j]
# 다음, 가로로 구해준 구간 합을 이용해 세로 구간 합을 구해준다
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[j][i] += prefix_sum[j-1][i]

# (r1, c1) 부터 (r2, c2)까지의 합
# prefix_sum[r2][c2] - prefix_sum[r1-1][c2] - prefix_sum[r2][c1-1] + 겹치는 구간인 prefix_sum[r1-1][c1-1]
for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    ans = prefix_sum[r2][c2] - prefix_sum[r1-1][c2] - prefix_sum[r2][c1-1] + prefix_sum[r1-1][c1-1]
    print(ans)