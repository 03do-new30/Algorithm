import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

ladders = [-1] * 100
for _ in range(n):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    ladders[x] = y
snakes = [-1] * 100
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -=1
    snakes[u] = v

def bfs():
    count = [-1] * 100
    count[0] = 0
    q = deque([0])

    while q:
        x = q.popleft()

        for i in range(1, 7):
            new_x = x + i

            if new_x >= 100:
                break
            
            # 사다리 체크
            if ladders[new_x] != -1:
                new_x = ladders[new_x]
            # 뱀 체크
            elif snakes[new_x] != -1:
                new_x = snakes[new_x]
            
            if count[new_x] != -1:
                continue
            
            # 방문 표시
            count[new_x] = count[x] + 1
            # 큐 삽입
            q.append(new_x)
    
    return count[99]

ans = bfs()
print(ans)