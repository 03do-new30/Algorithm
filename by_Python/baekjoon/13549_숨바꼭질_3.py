import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

max = 100001
visited = [-1] * max
current_q = deque() # 시간이 0
next_q = deque() # 시간이 1

visited[n] = 0
current_q.append(n)

while current_q:
    x = current_q.popleft()
    # 순간이동
    if x * 2 < max and visited[x * 2] == -1:
        visited[x * 2] = visited[x]
        current_q.append(x * 2)
    # 걷기
    if 0 <=  x - 1 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        next_q.append(x-1)
    if x + 1 < max and visited[x + 1] == -1:
        visited[x + 1] = visited[x] + 1
        next_q.append(x + 1)
    
    if len(current_q) == 0:
        current_q = next_q
        next_q = deque()

print(visited[k])