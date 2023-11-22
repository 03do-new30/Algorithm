import sys
input = sys.stdin.readline
from collections import deque

a, b, c = map(int, input().split())

def solve(a, b, c):
    if (a + b + c) % 3 != 0:
        return 0
    
    # 비교할 작은 수, 큰 수에 대해 검사 이력이 있는지 저장
    visited_xy = [[False] * 1501 for _ in range(1501)]
    q = deque([(a, b, c)])
    x = min(a, b, c)
    y = max(a, b, c)
    visited_xy[x][y] = False

    while q:
        a, b, c = q.popleft()
        if a == b and b == c and a == c:
            return 1
        # ab
        if a != b:
            if a < b:
                tmp = (a*2, b-a, c)
            elif a > b:
                tmp = (a-b, b*2, c)
            x = min(tmp)
            y = max(tmp)
            if not visited_xy[x][y]:
                visited_xy[x][y] = True
                q.append(tmp)
        # ac
        if a != c:
            if a < c:
                tmp = (a*2, b, c-a)
            elif a > c:
                tmp = (a-c, b, c*2)
            x = min(tmp)
            y = max(tmp)
            if not visited_xy[x][y]:
                visited_xy[x][y] = True
                q.append(tmp)
        # bc
        if b != c:
            if b < c:
                tmp = (a, b*2, c-b)
            elif b > c:
                tmp = (a, b-c, c*2)
            x = min(tmp)
            y = max(tmp)
            if not visited_xy[x][y]:
                visited_xy[x][y] = True
                q.append(tmp)
    return 0

print(solve(a, b, c))