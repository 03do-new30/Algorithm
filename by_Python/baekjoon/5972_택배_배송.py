import sys
input = sys.stdin.readline

import heapq

INF = float('inf')
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))

# dijkstra
dist = [INF] * (n+1)
dist[1] = 0
hq = [(0, 1)]
heapq.heapify(hq)
while hq:
    tmp_dist, node = heapq.heappop(hq)
    for next_node, weight in graph[node]:
        if dist[next_node] > dist[node] + weight:
            dist[next_node] = dist[node] + weight
            heapq.heappush(hq, (dist[next_node], next_node))

print(dist[n])