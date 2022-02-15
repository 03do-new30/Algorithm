import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

visited = [False]*(F+1)


def bfs(S):
    # q에 (층, 버튼 수) 저장
    q = deque([(S, 0)])
    visited[S] = True

    while q:
        floor, btn = q.popleft()
        # G층에 도착
        if floor == G:
            return btn

        # U버튼
        if floor + U <= F:
            if not visited[floor + U]:
                q.append((floor + U, btn + 1))
                visited[floor + U] = True
        # G버튼
        if 1 <= floor - D:
            if not visited[floor - D]:
                q.append((floor - D, btn + 1))
                visited[floor - D] = True

    return "use the stairs"


print(bfs(S))
