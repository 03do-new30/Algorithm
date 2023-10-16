import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

max_len = 100000
visited = [-1] * (max_len + 1)
q = deque()

q.append(n)
visited[n] = 0

while q:
    n = q.popleft()
    if n == k:
        print(visited[n])
        break
    if 0 <= n - 1 and visited[n-1] == -1:
        visited[n-1] = visited[n] + 1
        q.append(n-1)
    if n + 1 <= max_len and visited[n+1] == -1:
        visited[n+1] = visited[n] + 1
        q.append(n+1)
    if n * 2 <= max_len and visited[n*2] == -1:
        visited[n*2] = visited[n] + 1
        q.append(n*2)