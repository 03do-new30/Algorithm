import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 섬 표시
island = 0
visited = [[False] * n for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs_island(r, c):
    q = deque([(r, c)])
    visited[r][c] = True
    arr[r][c] += island
    while q:
        r, c = q.popleft()
        for dir in dirs:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < n and 0 <= new_c < n:
                if arr[new_r][new_c] == 1 and not visited[new_r][new_c]:
                    visited[new_r][new_c] = True
                    arr[new_r][new_c] += island
                    q.append((new_r, new_c))

for r in range(n):
    for c in range(n):
        if not visited[r][c] and arr[r][c] == 1:
            bfs_island(r, c)
            island += 1

# bfs를 마친 후 현재 섬의 총 개수는 island 개

# 다른 섬으로 도착하는 최단거리를 찾는다
# 각 섬에서 물가에 있는 좌표들을 BFS 시작 지점으로 삼는다
start_points = dict()
for r in range(n):
    for c in range(n):
        if arr[r][c] == 0:
            continue
        
        island_sign = arr[r][c]
        # 물가에 있는지 검사한다
        for dir in dirs:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < n and 0 <= new_c < n:
                if arr[new_r][new_c] == 0:
                    # 물가에 있음
                    if island_sign in start_points:
                        start_points[island_sign].append((r, c))
                    else:
                        start_points[island_sign] = [(r, c)]
                    # 물가에 있는 것을 알았으므로 종료
                    break

# print("start_points", start_points)

shortest = 100000
def bfs_bridge(island_sign):
    
    global shortest

    q = deque()
    visited = [[False] * n for _ in range(n)]

    points = start_points[island_sign]
    for r, c in points:
        q.append((r, c, 0))
        visited[r][c] = True
    
    while q:
        r, c, bridge = q.popleft()
        for dir in dirs:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c]:
                if arr[new_r][new_c] == 0:
                    q.append((new_r, new_c, bridge + 1))
                    visited[new_r][new_c] = True
                elif arr[new_r][new_c] != island_sign:
                    shortest = min(shortest, bridge)
                    visited[new_r][new_c] = True

for i in range(1, island + 1):
    bfs_bridge(i)

print(shortest)