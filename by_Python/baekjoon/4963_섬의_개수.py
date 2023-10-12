import sys
from collections import deque
input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def bfs(r, c):
    q = deque([])
    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        for dir in dirs:
            dir_r, dir_c = dir
            new_r = r + dir_r
            new_c = c + dir_c
            if 0 <= new_r < h and 0 <= new_c < w:
                if not visited[new_r][new_c] and arr[new_r][new_c] == 1:
                    visited[new_r][new_c] = True
                    q.append((new_r, new_c))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0
    for r in range(h):
        for c in range(w):
            if not visited[r][c] and arr[r][c] == 1:
                count += 1
                bfs(r, c)
    
    print(count)
