import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())


def bfs(num):
    q = deque([])
    visited = set()
    q.append((num, 0))
    visited.add(num)

    while q:
        num, cnt = q.popleft()

        if num == B:
            return cnt + 1

        x = num*2
        y = num*10 + 1

        if x <= B and x not in visited:
            visited.add(x)
            q.append((x, cnt+1))

        if y <= B and y not in visited:
            visited.add(y)
            q.append((y, cnt+1))

    return -1


print(bfs(A))
