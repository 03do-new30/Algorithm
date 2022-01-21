import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for __ in range(h)]

"""
익을 때까지 며칠이 걸리는지 -> 어떻게 기록해야할지? 어떻게 카운트해야할지 고민했는데
[level][row][col] 주변에 있는 토마토들이 익는다면,
그 주변 위치의 값을 0에서 -> box[level][row][col]+1로 갱신한다
"""


def bfs(q):
    moves = [(-1, 0, 0), (1, 0, 0),
             (0, -1, 0), (0, 1, 0),
             (0, 0, -1), (0, 0, 1)]

    while q:
        level, row, col = q.popleft()

        for move in moves:
            lv = level + move[0]
            r = row + move[1]
            c = col + move[2]
            if 0 <= lv < h and 0 <= r < n and 0 <= c < m:
                if box[lv][r][c] == 0:
                    box[lv][r][c] = box[level][row][col] + 1
                    q.append((lv, r, c))
                """ (예시)
                3 3 1
                0 0 0 
                0 0 1
                1 0 0
                """


# 시간초과 해결법 -> deque에 토마토가 있는 모든 좌표를 넣고 시작
q = deque([])
answer = 0
for level in range(h):
    for row in range(n):
        for col in range(m):
            if box[level][row][col] == 1:
                q.append((level, row, col))

bfs(q)

# answer는 box에서의 최대값
answer = 0
for inner in box:
    for row in inner:
        for x in row:
            answer = max(answer, x)
answer -= 1

# 토마토가 모두 익지는 못할 때 -> 여전히 0이 존재하는가?
for inner in box:
    for row in inner:
        if 0 in row:
            answer = -1
            break

print(answer)
