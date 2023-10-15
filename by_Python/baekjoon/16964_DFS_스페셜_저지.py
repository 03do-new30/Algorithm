import sys
input = sys.stdin.readline

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

# 입력으로 주어진 DFS 방문순서를 활용해 인접리스트를 정렬
rank = [0] * n
for i in range(n):
    rank[order[i]] = i
# 정렬
for i in range(n):
    a[i].sort(key = lambda x : rank[x])

dfs_result = []
visited = [False] * n

def dfs(x):
    if visited[x]:
        return
    
    visited[x] = True
    dfs_result.append(x)

    for y in a[x]:
        dfs(y)


dfs(0)


success = True
for i in range(n):
    if dfs_result[i] == order[i]:
        continue
    else:
        success = False
        break

print(1 if success else 0)