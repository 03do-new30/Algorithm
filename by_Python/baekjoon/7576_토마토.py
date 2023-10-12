import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
# 0이면 아직 방문하지 않은 경우
tomatoes = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(red_tomatoes):
    # 이미 익어있는 토마토들을 큐에 먼저 넣고 시작한다
    q = deque(red_tomatoes)
    
    while q:
        r, c = q.popleft()
        for dir_r, dir_c in dirs:
            new_r = r + dir_r
            new_c = c + dir_c

            if 0 <= new_r < n and 0 <= new_c < m:
                if tomatoes[new_r][new_c] == 0:
                    tomatoes[new_r][new_c] = tomatoes[r][c] + 1
                    q.append((new_r, new_c))

red_tomatoes = []
for i in range(n):
    for j in range(m):
        # 모든 익은 토마토에서부터 동시에 시작해야한다
        if tomatoes[i][j] == 1:
            red_tomatoes.append((i, j))
bfs(red_tomatoes)

# 익지 않은 토마토가 있는지 체크
success = True
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            success = False
            break
    
if success:
    # 토마토가 모두 익을때까지의 최소 날짜 출력
    # tomatoes에서의 max값 -1 (이미 익어있는 토마토 1(사실상 0일차)에서부터 +1, +1,,, 했으므로)
    answer = max(map(max, tomatoes))
    print(answer - 1)
else:
    print(-1)
