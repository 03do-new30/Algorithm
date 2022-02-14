import sys
input = sys.stdin.readline


dp = [[[None]*21 for _ in range(21)] for _ in range(21)]
# dp[0][0][0] = 1로 초기화
dp[0][0][0] = 1


def solve(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return dp[0][0][0]

    if a > 20 or b > 20 or c > 20:
        return solve(20, 20, 20)

    if dp[a][b][c] is not None:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = solve(a, b, c-1) + solve(a, b-1, c-1) - solve(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = solve(a-1, b, c) + solve(a-1, b-1, c) + \
        solve(a-1, b, c-1) - solve(a-1, b-1, c-1)
    return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    ans = solve(a, b, c)

    print(f"w({a}, {b}, {c}) = {ans}")
