# 1967_트리의 지름과 유사
import sys
import heapq
input = sys.stdin.readline

V = int(input().strip())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    info = list(map(int, input().split()))

    # 정점 번호
    u = info[0]

    idx = 1
    while info[idx] != -1:
        v = info[idx]
        wt = info[idx+1]
        # graph
        graph[u].append((v, wt))
        # update
        idx += 2


def dfs(start, dist):
    if visited[start]:
        return

    # heapq에 (-거리, 정점) 으로 삽입
    heapq.heappush(q, (-dist, start))
    visited[start] = True

    for x in graph[start]:
        node, weight = x
        dfs(node, dist + weight)


# min heap을 max heap처럼 사용하기 위해서, heapq에 (-거리, 정점) 으로 삽입한다
q = []
visited = [False]*(V+1)
# 임의의 정점에서 가장 먼 정점을 고른다
# 정점 1에서 가장 먼 정점을 고른다
dfs(1, 0)
max_dist_node = heapq.heappop(q)[1]

# 임의의 정점에서 가장 먼 정점 max_dist_node에서
# 가장 먼 정점까지의 거리가 트리의 지름이다
q = []
visited = [False]*(V+1)
dfs(max_dist_node, 0)
max_dist = -heapq.heappop(q)[0]  # 음수로 바꿔둔 것 해제

print(max_dist)
