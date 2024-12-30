import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]

target = input().strip()

# dp[r][c][i] = (r, c) 위치의 알파벳이 target[i]와 같을 때, 
# (r, c) 위치까지의 경로의 수

# dp[r][c][i] = (r, c)에서 k칸 내에 이동할 수 있는 
# 모든 칸 (prev_r, prev_c)에 대해
# sum(dp[prev_r][prev_c][i-1])
dp = [[[0] * len(target) for _ in range(m)] for __ in range(n)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def solve(idx):
    for r in range(n):
        for c in range(m):
            if arr[r][c] == target[idx]:
                if idx == 0:
                    dp[r][c][idx] += 1
                    continue
                # k칸 내로 이동할 수 있는 모든 칸에 대해
                for i in range(4):
                    for cnt in range(1, k+1):
                        prev_r = r + dr[i] * cnt
                        prev_c = c + dc[i] * cnt
                        if prev_r < 0 or prev_r >= n or prev_c < 0 or prev_c >= m:
                            continue
                        if arr[prev_r][prev_c] == target[idx - 1]:
                            dp[r][c][idx] += dp[prev_r][prev_c][idx-1]

for i in range(len(target)):
    solve(i)


# 경로의 개수 구하기
ans = 0
for r in range(n):
    for c in range(m):
        ans += dp[r][c][len(target) - 1]

print(ans)