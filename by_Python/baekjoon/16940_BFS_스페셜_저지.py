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

visited = [False] * n
parent = [-1] * n
q = deque()

# 시작점
q.append(0)
visited[0] = True
total = 1

for i in range(n):
    if not q:
        print(0)
        exit()
    
    x = q.popleft()
    if x != order[i]:
        print(0)
        exit()
    
    x_possible_nodes = 0
    for y in a[x]:
        if not visited[y]:
            parent[y] = x
            x_possible_nodes += 1
    
    for j in range(x_possible_nodes):
        if total + j >= n:
            print(0)
            exit()
        
        if parent[order[total + j]] != x:
            print(0)
            exit()
        
        q.append(order[total + j])
        visited[order[total + j]] = True
    
    total += x_possible_nodes

print(1)