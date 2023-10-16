import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)] # 벽을 부순 횟수를 저장

# BFS
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited[0][0] = 0
current_q = deque([(0, 0)]) # 부순 벽이 없을 떄
next_q = deque() # 부순 벽이 있을 때
while current_q:
    r, c = current_q.popleft()
    for dir in dirs:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < m and 0 <= new_c < n:
            if visited[new_r][new_c] == -1:
                # 빈방
                if arr[new_r][new_c] == 0:
                    visited[new_r][new_c] = visited[r][c]
                    current_q.append((new_r, new_c))
                # 벽
                else:
                    visited[new_r][new_c] = visited[r][c] + 1
                    next_q.append((new_r, new_c))
    
    if len(current_q) == 0:
        current_q = next_q
        next_q = deque()

print(visited[m-1][n-1])