import sys
input = sys.stdin.readline
from collections import deque

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

n = int(input())
r, c, goal_r, goal_c = map(int, input().split())

def bfs(r, c, goal_r, goal_c):
    count = [[-1] * n for _ in range(n)]
    count[r][c] = 0
    q = deque([(r, c)])

    while q:
        r, c = q.popleft()
        if r == goal_r and c == goal_c:
            break
        for i in range(6):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < n and 0 <= new_c < n:
                if count[new_r][new_c] == -1:
                    count[new_r][new_c] = count[r][c] + 1
                    q.append((new_r, new_c))
    
    return count[goal_r][goal_c]

print(bfs(r, c, goal_r, goal_c))