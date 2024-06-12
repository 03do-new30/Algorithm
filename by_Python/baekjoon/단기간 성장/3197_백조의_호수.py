"""
[단기간 실력 향상]
- 시간초과를 피하기 위해 사용한 큐 여러개 유지하는 기법 기억
"""

from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 백조에 대한 현재 큐, 백조에 대한 넥스트 큐
swan_q = deque()
swan_next_q = deque()
# 물에 대한 현재 큐, 물에 대한 넥스트 큐
water_q = deque()
water_next_q = deque()
# 방문 표시
visited = [[False] * m for _ in range(n)]

# 백조에 대한 BFS
def swan_bfs():
    while swan_q:
        r, c = swan_q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc]:
                    if arr[nr][nc] == 'L': # 백조를 만남
                        return True
                    elif arr[nr][nc] == '.': # 물
                        visited[nr][nc] = True
                        swan_q.append((nr, nc))
                    else: # 빙판
                        # 다음에 여기서부터 검사할 것이므로 next_q에 저장
                        swan_next_q.append((nr, nc))
                        visited[nr][nc] = True
    return False

# 물에 대한 BFS
def water_bfs():
    while water_q:
        r, c = water_q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 'X': # 빙판
                    # 물로 바꿔주고
                    arr[nr][nc] = '.'
                    # 다음 큐에 삽입
                    water_next_q.append((nr, nc))

# swan_q 초기화
found_one = False
for r in range(n):
    if found_one:
        break
    for c in range(m):
        if arr[r][c] == 'L':
            swan_q.append((r, c))
            visited[r][c] = True
            found_one = True
            break

# water_q 초기화
for r in range(n):
    for c in range(m):
        if arr[r][c] != 'X':
            water_q.append((r, c))
day = 0
while True:
    # 백조 만날 수 있는지 검사
    can_meet = swan_bfs()
    if can_meet:
        print(day)
        break
    # print("swan_next_q:", swan_next_q)

    # update
    swan_q = swan_next_q
    swan_next_q = deque()
    # 빙판 녹이기
    water_bfs()
    # print("water_next_q:", water_next_q)
    # update
    water_q = water_next_q
    water_next_q = deque()
    # print('-' * 30)
    
    day += 1