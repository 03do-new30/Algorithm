# n: 미로의 세로 길이
# m: 미로의 가로 길이
# (x, y): 출발지점
# (r, c): 도착지점
# k: (x, y)애서 (r, c)까지 이동하는 거리가 총 k여야 한다
from collections import deque

def solution(n, m, x, y, r, c, k):
    
    # 사전순으로 빠른 경로로 탈출해야하므로 탐색 순서는
    # d(아래) -> l(왼) -> r(오) -> u(위)
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    direction = {0:'d', 1:'l', 2:'r', 3:'u'}

    q = deque()
    q.append((x, y, "", k)) # (row, col, 기록, 남은 거리)
    visited = [] # 방문 기록들
    visited.append((x, y, ""))
    while q:
        row, col, log, remain = q.popleft()
        if row == r and col == c:
            # 남아있는 거리가 홀수라면 왔다갔다해서 다시 도착지점으로 올 수 없음
            if remain % 2 == 1:
                return "impossible"
            if remain == 0:
                return log
        
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 1 <= nr < n+1 and 1 <= nc < m+1:
                # 앞으로 가야할 거리가 k를 초과한다면 올바른 이동 루트가 아님
                if abs(nr - r) + abs(nc - c) + len(log) > k:
                    continue
                q.append((nr, nc, log + direction[i], remain - 1))
                # q에 경로가 하나만 추가된다면 break 걸어도 됨
                # -> 처음 추가되는 경로가 어차피 사전순으로 가장 빠른 이동 경로! 우리는 지금 d->l->r->u순으로 검사하고 있음!
                # 만약 d로 가는 경로가 있다면, 그 뒤 경로들은 확인하지 않아도 됨
                break
    
    return "impossible"

n = [3, 2, 3]
m = [4, 2, 3]
x = [2, 1, 1]
y = [3, 1, 2]
r = [3, 2, 3]
c = [1, 2, 3]
k = [5, 2, 4]
result = ["dllrl", "dr", "impossible"]
for i in range(len(n)):
    print(result[i] == solution(n[i], m[i], x[i], y[i], r[i], c[i], k[i]))
    print('-' * 40)