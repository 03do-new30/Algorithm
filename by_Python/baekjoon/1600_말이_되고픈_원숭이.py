import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    # visited[r][c][k] = (r, c)에 능력을 k번 사용해서 왔을 때, 말의 움직임 횟수
    visited = [[[-1]*(K+1) for _ in range(W)] for _ in range(H)]
    q = deque([(0, 0, 0, 0)]) # (r, c, 움직임횟수, 능력사용횟수)
    visited[0][0][0] = 0

    # 상하좌우
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    # 말의 움직임
    kr = [-2, -2, -1, -1, 1, 1, 2, 2]
    kc = [1, -1, 2, -2, 2, -2, -1, 1]

    while q:
        r, c, move, count = q.popleft()
        # 상, 하, 좌, 우
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < H and 0 <= nc < W:
                if board[nr][nc] == 0 and visited[nr][nc][count] == -1:
                    visited[nr][nc][count] = move + 1
                    q.append((nr, nc, move + 1, count))

        
        if count < K:
            # 말의 움직임
            for i in range(8):
                nr, nc = r + kr[i], c + kc[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if board[nr][nc] == 0 and visited[nr][nc][count+1] == -1:
                        visited[nr][nc][count+1] = move + 1
                        q.append((nr, nc, move + 1, count + 1))

    # visited[H-1][W-1]에서 값이 -1이 아닌 것 중 최소값을 구한다
    candidates = []
    for x in visited[H-1][W-1]:
        if x > -1:
            candidates.append(x)
    if candidates:
        return min(candidates)
    return -1



K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
# (0, 0) ~ (H-1, W-1)까지 가야 함

print(bfs())

"""
1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
"""