import sys
input = sys.stdin.readline
import heapq

INF = float('inf')

def dijkstra(s):
    dist = [INF] * (n+1)
    dist[s] = 0
    hq = [(0, s)]
    heapq.heapify(hq)

    while hq:
        node_wt, node = heapq.heappop(hq)
        for next_node, weight in graph[node]:
            if weight + node_wt < dist[next_node]:
                dist[next_node] = weight + node_wt
                heapq.heappush(hq, (weight + node_wt, next_node))
    return dist


for _ in range(int(input())):
    # n: 노드 개수, m: 간선 개수, t: 목적지 후보 개수
    n, m, t = map(int, input().split())
    # s: 출발지, g-h 간선은 반드시 지나는 간선임
    s, g, h = map(int, input().split())

    GH = 0 # g-h 간선의 거리

    # 그래프 생성 - 인접리스트
    graph = [[] for _ in range(n + 1)]
    for __ in range(m):
        # a와 b 사이에 거리 d인 간선이 있음
        a, b, d = map(int, input().split())
        graph[a].append((b, d)) # (노드, 거리)
        graph[b].append((a, d))
        if (a == g and b == h) or (a == h and b == g):
            GH = d
    
    # 목적지 후보
    candidates = []
    for __ in range(t):
        candidates.append(int(input()))
    candidates.sort()
    
    # s에서의 dijkstra 최단거리 결과
    s_dist = dijkstra(s)
    # g에서의 dijkstra 최단거리 결과
    g_dist = dijkstra(g)
    # h에서의 dijkstra 최단거리 결과
    h_dist = dijkstra(h)

    # s -> target = (s -> g) + (g-h: GH) + (h -> target)
    # s -> target = (s -> h) + (h-g: GH) + (g -> target)
    
    answer = []
    for target in candidates:
        # 주의!!! INF == INF + INF
        if s_dist[target] == INF:
            continue
        if s_dist[target] == GH + min(s_dist[g] + h_dist[target], s_dist[h] + g_dist[target]):
            answer.append(target)

    print(' '.join(list(map(str, answer))))