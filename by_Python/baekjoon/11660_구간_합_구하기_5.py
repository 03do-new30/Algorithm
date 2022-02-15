# 참고: https://claude-u.tistory.com/427
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]


# 누적합

# version 1
# prefix_sum[r][c]: r행의 1번째 열의 숫자부터 c번째 열의 숫자까지의 합
prefix_sum = [[0]*(N+1) for _ in range(N+1)]
for r in range(1, N+1):
    for c in range(1, N+1):
        prefix_sum[r][c] = prefix_sum[r][c-1] + arr[r][c]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for r in range(x1, x2+1):
        ans += prefix_sum[r][y2] - prefix_sum[r][y1-1]
    print(ans)


# version 2
# prefix_sum[r][c]: (1, 1,)부터 (r, c)까지의 합
prefix_sum = [[0]*(N+1) for _ in range(N+1)]
for r in range(1, N+1):
    for c in range(1, N+1):
        prefix_sum[r][c] = prefix_sum[r-1][c] + \
            prefix_sum[r][c-1] - prefix_sum[r-1][c-1] + arr[r][c]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - \
        prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
    print(ans)
