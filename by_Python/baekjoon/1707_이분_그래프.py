from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, visited):
    q = deque([start])
    visited[start] = "red"

    while q:
        u = q.popleft()
        for v in graph[u]:
            # 아직 방문하지 않음
            if visited[v] == "":
                if visited[u] == "red":
                    visited[v] = "blue"
                else:
                    visited[v] = "red"
                q.append(v)
            # 방문한 그래프라면
            # u와 v의 색깔이 같으면 안됨
            elif visited[v] == visited[u]:
                return "NO"
    return "YES"


K = int(input().strip())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for __ in range(V+1)]
    for __ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    """ graph print """
    """
    print("="*10, "graph", "="*10)
    for row in graph:
        print(row)
    """

    """ visited """
    visited = [""] * (V+1)

    """ bfs """
    # 모든 정점이 연결되어 있지 않을 수도 있으므로
    # 각 정점을 한 번 씩 검사해줘야 함
    for i in range(1, V+1):
        if visited[i] == "":
            ans = bfs(i, visited)
            if ans == "NO":
                # ans가 NO라면 바로 탐색 멈추고 프린트
                break
    print(ans)
