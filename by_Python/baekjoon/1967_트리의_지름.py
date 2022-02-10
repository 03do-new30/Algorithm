import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


n = int(input().strip())
graph = [[] for _ in range(n+1)]


def dfs(u, wt):
    for x in graph[u]:
        v = x[0]
        v_wt = x[1]

        if dist[v] == -1:
            dist[v] = wt + v_wt
            dfs(v, dist[v])


for _ in range(n-1):
    u, v, wt = map(int, input().split())
    graph[u].append((v, wt))
    graph[v].append((u, wt))

# 임의의 노드에서 가장 먼 곳 x를 찾고,
# 그 x에서 가장 먼 곳 y를 찾는다.
# x - y의 거리가 트리의 지름이 된다.
dist = [-1]*(n+1)

# 노드 1에서 가장 먼 노드를 찾는다
dist[1] = 0
dfs(1, 0)

# 노드 1에서 가장 먼 노드 furthest에서 가장 먼 노드를 찾는다
furthest = dist.index(max(dist))
dist = [-1]*(n+1)
dist[furthest] = 0
dfs(furthest, 0)

# 출력
print(max(dist))
