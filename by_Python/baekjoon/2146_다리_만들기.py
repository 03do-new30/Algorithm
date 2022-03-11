# https://kyun2da.github.io/2021/04/22/makeBridge/
from collections import deque
import sys
input = sys.stdin.readline


def mark_island(r, c, num):
    arr[r][c] = num
    q = deque([(r, c)])

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > 0 and not visited[nr][nc]:
                    arr[nr][nc] = num
                    q.append((nr, nc))
                    visited[nr][nc] = True


def make_bridge(num):
    global ans

    dist = [[-1]*N for _ in range(N)]  # 거리가 저장되는 배열
    q = deque()

    for r in range(N):
        for c in range(N):
            # 번호 num인 섬에 속하는 좌표들을 q에 삽입
            if arr[r][c] == num:
                q.append((r, c))
                dist[r][c] = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                # 다른 섬
                if arr[nr][nc] > 0 and arr[nr][nc] != num:
                    ans = min(ans, dist[r][c])
                    return
                # 바다
                if arr[nr][nc] == 0 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))


N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 가장 짧은 다리의 길이
ans = 10000

# 섬에 번호 매기기
visited = [[False]*N for _ in range(N)]
island_num = 1
for r in range(N):
    for c in range(N):
        # 섬을 1, 2, 3... 번호 매긴다
        if arr[r][c] == 1 and not visited[r][c]:
            mark_island(r, c, island_num)
            island_num += 1

# 다리 놓기
for i in range(1, island_num):
    make_bridge(i)

print(ans)
