import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

max = 100001
visited = [-1] * max
q = deque()

visited[n] = 0
q.append(n)

# 순간이동할 경우에는 큐의 앞에,
# 걸어서 이동하는 경우에는 큐의 뒤에

while q:
    x = q.popleft()
    # 순간이동
    if x * 2 < max and visited[x * 2] == -1:
        visited[x * 2] = visited[x]
        q.appendleft(x * 2)
    # 걷기
    if 0 <=  x - 1 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
    if x + 1 < max and visited[x + 1] == -1:
        visited[x + 1] = visited[x] + 1
        q.append(x + 1)
print(visited[k])