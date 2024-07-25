import sys
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

# 시작점
start_loc = (0, 0)
# 종료지점
end_loc = (0, 0)

first = True
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'C':
            if first:
                first = False
                start_loc = (r, c)
            else:
                end_loc = (r, c)
                break


# 레이저의 방향: 0=좌, 1=우, 2=상, 3=하
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# mirrors[r][c] = (r, c) 위치까지 오는 데 필요한 거울의 최소 개수
mirrors = [[-1] * m for _ in range(n)]
q = deque([(start_loc[0], start_loc[1], 0)])
mirrors[start_loc[0]][start_loc[1]] = 0
while q:
    r, c, mirror = q.popleft()
    for i in range(4):
        nr = r
        nc = c 
        while 0 <= nr + dr[i] < n and 0 <= nc + dc[i] < m:
            nr += dr[i]
            nc += dc[i]
            if arr[nr][nc] == '*':
                break
            if mirrors[nr][nc] > -1 and mirrors[nr][nc] <= mirror + 1:
                continue
            mirrors[nr][nc] = mirror + 1
            q.append((nr, nc, mirror + 1))

answer = mirrors[end_loc[0]][end_loc[1]] - 1
print(answer)
