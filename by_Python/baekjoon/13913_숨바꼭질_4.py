import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
max = 100001
visited = [-1] * max # -1이면 미방문, 아니면 시간 저장
parent = [-1] * max # 어떤 노드에서부터 도착했는지를 저장

# bfs
q = deque([n])
visited[n] = 0
parent[n] = -1

while q:
    n = q.popleft()
    if 0 <= n - 1 and visited[n-1] == -1:
        visited[n-1] = visited[n] + 1
        q.append(n-1)
        parent[n-1] = n
    if n + 1 < max and visited[n+1] == -1:
        visited[n+1] = visited[n] + 1
        q.append(n+1)
        parent[n+1] = n
    if n * 2 < max and visited[n*2] == -1:
        visited[n*2] = visited[n] + 1
        q.append(n*2)
        parent[n*2] = n

print(visited[k])
# 경로 만들기
node = k
path = []
while True:
    if parent[node] == -1:
        path.append(node)
        break

    path.append(node)
    node = parent[node]

path.reverse()
print(' '.join(list(map(str, path))))