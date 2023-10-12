import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 현재까지의 칸수를 저장
step = [[0]*m for _ in range(n)] # 0이면 미방문
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(r, c):
    q = deque([])
    q.append((r, c))
    step[r][c] = 1

    while q:
        r, c = q.popleft()
        for dir_r, dir_c in dirs:
            new_r = r + dir_r
            new_c = c + dir_c
            if 0 <= new_r < n and 0 <= new_c < m:
                if step[new_r][new_c] == 0 and maze[new_r][new_c] == 1:
                    step[new_r][new_c] = step[r][c] + 1
                    q.append((new_r, new_c))

bfs(0, 0)
print(step[n-1][m-1])