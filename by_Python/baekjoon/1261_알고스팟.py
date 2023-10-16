import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)] # 벽을 부순 횟수를 저장

# BFS
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited[0][0] = 0
# 방으로 이동하는 경우는 데크의 앞에
# 벽을 부수고 이동하는 경우는 데크의 뒤에
q = deque([(0, 0)])

while q:
    r, c = q.popleft()
    for dir in dirs:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < m and 0 <= new_c < n:
            if visited[new_r][new_c] == -1:
                # 빈방
                if arr[new_r][new_c] == 0:
                    visited[new_r][new_c] = visited[r][c]
                    q.appendleft((new_r, new_c))
                # 벽
                else:
                    visited[new_r][new_c] = visited[r][c] + 1
                    q.append((new_r, new_c))

print(visited[m-1][n-1])