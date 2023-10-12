import sys
input = sys.stdin.readline
from collections import deque

dirs = [(-2, -1), (-1, -2),
        (-2, 1), (-1, 2),
        (1, -2), (2, -1),
        (1, 2), (2, 1)]
def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        for dir_r, dir_c in dirs:
            new_r = r + dir_r
            new_c = c + dir_c
            if 0 <= new_r < n and 0 <= new_c < n:
                if visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = visited[r][c] + 1
                    q.append((new_r, new_c))



tc = int(input())
for _ in range(tc):
    n = int(input())
    # 현재칸
    r, c = map(int, input().split())
    # 이동하려는 칸
    target_r, target_c = map(int, input().split())

    visited = [[0] * n for _ in range(n)]
    bfs(r, c)
    print(visited[target_r][target_c] - 1)
