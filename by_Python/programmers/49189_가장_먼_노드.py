from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        u, v = e
        graph[u].append(v)
        graph[v].append(u)
    visited = [-1] * (n+1)
    q = deque([1])
    visited[1] = 0
    max_dist = 0
    max_dist_cnt = 0
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1 or visited[next_node] > visited[node] + 1:
                visited[next_node] = visited[node] + 1
                if max_dist < visited[next_node]:
                    max_dist = visited[next_node]
                    max_dist_cnt = 1
                elif max_dist == visited[next_node]:
                    max_dist_cnt += 1
                q.append(next_node)
    return max_dist_cnt

n = [6]
vertex = [[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]]
result = [3]
for i in range(len(result)):
    print(solution(n[i], vertex[i]) == result[i])