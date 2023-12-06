import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

size = 2
stomach = 0

def bfs(r, c):
    global size, stomach

    q = deque([(r, c)])
    visited = [[-1] * n for _ in range(n)] # 칸에 도달할 때까지 걸린 시간
    visited[r][c] = 0
    # 상, 좌, 우, 하 순서
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]
    # 먹을 수 있는 물고기를 저장해보자
    fishes = [] # (도달할 때 까지 걸린 시간,물고기 r, 물고기 c)
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc] > -1:
                    continue
                # 지나갈 수 있는 칸
                if arr[nr][nc] ==0 or arr[nr][nc] == size and visited[nr][nc] == -1:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                # 먹을 수 있는 물고기
                elif 0 < arr[nr][nc] < size:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                    fishes.append((visited[r][c] + 1, nr, nc))
    if len(fishes) == 0:
        return -1, -1, -1 # 물고기를 잡아먹을 수 없을 때
    
    # 저장한 물고기를 정렬해서 먹을 물고기를 정한다
    fishes.sort()
    meal_time, meal_r, meal_c = fishes[0]
    # 사이즈 조정
    if stomach + 1 == size:
        size += 1
        stomach = 0
    else:
        stomach += 1
    return meal_r, meal_c, meal_time


shark_r = -1; shark_c = -1
for x in range(n):
    for y in range(n):
        if arr[x][y] == 9:
            shark_r = x; shark_c = y
            break

# 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
answer = 0
while True:
    fish_r, fish_c, fish_time = bfs(shark_r, shark_c)
    if fish_time == -1:
        break

    arr[fish_r][fish_c] = 9 # 원래 물고기가 있던 자리는 상어 자리
    arr[shark_r][shark_c] = 0 # 원래 상어가 있던 자리는 빈칸
    answer += fish_time # 물고기를 잡아먹는 데 걸리는 시간 합산
    
    shark_r = fish_r; shark_c = fish_c # 값 교체

print(answer)