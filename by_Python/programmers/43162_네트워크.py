from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        print(visited)
        if not visited[i]:
            bfs(i, visited, computers)
            answer += 1
    return answer


def bfs(start, visited, computers):
    q = deque([start])
    visited[start] = True

    while q:
        u = q.popleft()
        for v in range(len(computers)):
            if computers[u][v] == 1 and not visited[v]:
                q.append(v)
                visited[v] = True


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
