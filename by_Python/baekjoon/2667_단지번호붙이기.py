import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(i, j):
    q = deque([])
    q.append((i, j))
    visited[i][j] = True

    count = 0
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        i, j = q.popleft()
        count += 1

        for dir_i, dir_j in dirs:
            new_i = i + dir_i
            new_j = j + dir_j
            if 0 <= new_i < n and 0 <= new_j < n:
                if arr[new_i][new_j] == 1 and not visited[new_i][new_j]:
                    q.append((new_i, new_j))
                    visited[new_i][new_j] = True

    return count

danji = 0
counts = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            danji += 1
            count = bfs(i, j)
            counts.append(count)

print(danji)
counts.sort()
for count in counts:
    print(count)