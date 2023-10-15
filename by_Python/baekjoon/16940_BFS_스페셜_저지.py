import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

order = list(map(int, input().split()))
order = [x-1 for x in order]

# 입력으로 주어진 순서를 이용해 인접 리스트를 정렬한 뒤
# BFS를 실행
rank = [0] * n

for i in range(n):
    rank[order[i]] = i

# 인접리스트 정렬
for i in range(n):
    a[i].sort(key = lambda x : rank[x])

bfs_result = []
q = deque()
visited = [False] * n

q.append(0)
visited[0] = True

while q:
    x = q.popleft()
    bfs_result.append(x)
    for y in a[x]:
        if not visited[y]:
            q.append(y)
            visited[y] = True

success = True
for i in range(n):
    if bfs_result[i] == order[i]:
        continue
    else:
        success = False
        break

print(1 if success else 0)