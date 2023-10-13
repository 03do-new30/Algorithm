import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 색 color의 한 점에서 상, 하, 좌, 우로 DFS를 한다
# 이전칸으로 가지 않게 DFS를 한다!
# 만약 언젠가 방문했던 칸으로 도착한다면, cycle이 있다고 볼 수 있다
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(r, c, past_r, past_c, color):
    if visited[r][c]:
        return True
    
    visited[r][c] = True

    for rr, cc in dirs:
        new_r = r + rr
        new_c = c + cc
        if 0 <= new_r < n and 0 <= new_c < m:
            if new_r == past_r and new_c == past_c:
                continue
            else:
                if arr[new_r][new_c] == color:
                    ret = dfs(new_r, new_c, r, c, color)
                    if ret:
                        return True
    
    return False

for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            cycle = dfs(r, c, -1, -1, arr[r][c])
            if cycle: # cycle 존재
                print("Yes")
                exit()
print("No")