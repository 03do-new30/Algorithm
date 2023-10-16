import sys
input = sys.stdin.readline
from collections import deque

target_s = int(input())

visited = [[False] * 1001 for _ in range(1001)]
time = [[0] * 1001 for _ in range(1001)]

# 정점을 클립보드의 상태마다 관리해줘야한다!
# (s, c) = (화면에 s개, 클립보드에 c개)
# (1, 0) = 시작점

# BFS
q = deque([(1, 0)])
visited[1][0] = True

while q:
    s, c = q.popleft()
    # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
    if not visited[s][s]:
        visited[s][s] = 1
        time[s][s] = time[s][c] + 1
        q.append((s, s))
    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기함
    if c > 0:
        next_s = s + c
        if next_s <= 1000 and not visited[next_s][c]:
            visited[next_s][c] = True
            time[next_s][c] = time[s][c] + 1
            q.append((next_s, c))
    # 3. 화면에 있는 이모티콘 중 하나를 삭제한다
    if 0 <= s - 1:
        next_s = s - 1
        if not visited[next_s][c]:
            visited[next_s][c] = True
            time[next_s][c] = time[s][c] + 1
            q.append((next_s, c))

# time[target_s] 에서 최솟값을 구해본다
min_time = 1000000
for c in range(1001):
    if visited[target_s][c]:
        min_time = min(min_time, time[target_s][c])

print(min_time)
