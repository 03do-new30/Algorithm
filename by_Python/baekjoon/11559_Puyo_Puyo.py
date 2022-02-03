from collections import deque
import sys
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(12)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(r, c, visited):
    q = deque([(r, c)])
    visited[r][c] = True
    tmp_puyo = [(r, c)]

    while q:
        r, c = q.popleft()
        color = arr[r][c]

        for move in moves:
            new_r = r + move[0]
            new_c = c + move[1]
            if 0 <= new_r < 12 and 0 <= new_c < 6:
                if not visited[new_r][new_c]:
                    if arr[new_r][new_c] == color:
                        visited[new_r][new_c] = True
                        q.append((new_r, new_c))
                        tmp_puyo.append((new_r, new_c))

    return tmp_puyo


def move_puyos(puyos):
    # 터지는 뿌요가 있는 칸을 빈칸으로 만듦
    for puyo in puyos:
        arr[puyo[0]][puyo[1]] = "."

    # 맨 아래 row부터 위로 탐색해가야 함
    for r in range(11, -1, -1):
        for c in range(6):
            if arr[r][c] != '.':
                new_r = r
                while 0 <= new_r + 1 < 12:
                    if arr[new_r+1][c] == '.':
                        new_r += 1
                    else:
                        break
                if r < new_r:
                    arr[new_r][c] = arr[r][c]
                    arr[r][c] = '.'


# 연쇄 카운트
cnt = 0
visited = [[False]*6 for _ in range(12)]
puyos = []  # 이번 턴에 터지는 뿌요들의 위치를 저장한다

# while loop 한 번 돌면 = 한 턴
while True:
    for r in range(12):
        for c in range(6):
            if arr[r][c] != '.' and not visited[r][c]:
                tmp_puyo = bfs(r, c, visited)
                if len(tmp_puyo) >= 4:
                    puyos += tmp_puyo

    # 터질 수 있는 뿌요가 하나도 없으면 while 중단
    if len(puyos) == 0:
        break

    if len(puyos) >= 4:
        # 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.
        # 연쇄 카운트 + 1
        cnt += 1
        # 뿌요들이 내려옴
        move_puyos(puyos)

    # visited 초기화
    visited = [[False]*6 for _ in range(12)]
    # puyos 초기화
    puyos = []


print(cnt)
