from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 물이 차는 시간을 기록
water = [[0]*C for _ in range(R)]


def water_bfs(row, col, water_visited):
    q = deque([(row, col)])
    water_visited[row][col] = True
    water[row][col] = 0
    while q:
        row, col = q.popleft()
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]

            if 0 <= new_row < R and 0 <= new_col < C:
                if not water_visited[new_row][new_col]:
                    if arr[new_row][new_col] == '.':
                        # water에 물이 차는 시간 기록이 없을 때
                        if water[new_row][new_col] == 0:
                            water[new_row][new_col] = water[row][col] + 1
                        # water에 물이 차는 시간 기록이 있다면 min값으로 갱신한다
                        elif water[new_row][new_col] > 0:
                            water[new_row][new_col] = min(
                                water[new_row][new_col], water[row][col] + 1)
                        water_visited[new_row][new_col] = True
                        q.append((new_row, new_col))


# 고슴도치가 움직이는 시간을 기록
visited = [[0]*C for _ in range(R)]


def bfs(row, col):
    q = deque([(row, col)])
    visited[row][col] = 0

    while q:
        row, col = q.popleft()
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < R and 0 <= new_col < C:
                if not visited[new_row][new_col]:
                    # 비어 있는 곳인가?
                    if arr[new_row][new_col] == '.':
                        # 물이 차지는 않았는가?
                        # 다음 움직일 곳이 물이 차있지 않아야한다
                        # 아예 물이 들어와있지 않거나, 물이 들어오기 전에 고슴도치가 지나감
                        if water[new_row][new_col] == 0 or water[new_row][new_col] > visited[row][col] + 1:
                            visited[new_row][new_col] = visited[row][col] + 1
                            q.append((new_row, new_col))
                    # 비버의 굴인가?
                    elif arr[new_row][new_col] == 'D':
                        visited[new_row][new_col] = visited[row][col] + 1
                        q.append((new_row, new_col))


for r in range(R):
    for c in range(C):
        if arr[r][c] == '*':
            tmp_visited = [[False]*C for _ in range(R)]
            water_bfs(r, c, tmp_visited)

""" water 출력
for water_row in water:
    print(water_row)
"""

for r in range(R):
    for c in range(C):
        if arr[r][c] == 'S':
            bfs(r, c)

""" visited 출력
print('-'*15)
for visited_row in visited:
    print(visited_row)
"""

# 비버의 굴로 가는 시간 구하기
ans = 0
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'D':
            ans = visited[r][c]
            break
if ans == 0:
    print("KAKTUS")
else:
    print(ans)
