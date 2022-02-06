# 참고: https://wlstyql.tistory.com/72
# 참고: https://rebas.kr/724
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find(str):
    # str의 좌표 찾기
    for r in range(N):
        for c in range(M):
            if board[r][c] == str:
                return (r, c)
    return None


def move(x, y, dx, dy):
    # 이동 횟수
    steps = 0
    while board[x][y] != 'O' and board[x+dx][y+dy] != '#':
        x += dx
        y += dy
        steps += 1
    return x, y, steps


def bfs(rx, ry, bx, by):
    cnt = 1
    q = deque([(rx, ry, bx, by, cnt)])
    visited[rx][ry][bx][by] = True

    while q:
        rx, ry, bx, by, cnt = q.popleft()

        # 10번 이하로 움직여서 빨간 구슬을 빼낼 수 없다
        if cnt > 10:
            break

        for i in range(4):
            new_rx, new_ry, r_steps = move(rx, ry, dx[i], dy[i])
            new_bx, new_by, b_steps = move(bx, by, dx[i], dy[i])

            # (new_bx, new_by)가 구멍이 아니면 (실패 조건 만족 X)
            if board[new_bx][new_by] != 'O':
                # (new_rx, new_ry)가 구멍이라면 (성공 조건 만족 O)
                if board[new_rx][new_ry] == 'O':
                    print(cnt)
                    return

                # 기울인 후 빨간 구슬과 파란 구슬이 같은 위치에 있다면
                if new_rx == new_bx and new_ry == new_by:
                    # steps가 적은 것이 더 먼저 도착.
                    # steps가 더 큰 색의 구슬을 dx dy만큼 움직이기 이전 위치로 되돌려놓음
                    if r_steps < b_steps:
                        new_bx -= dx[i]
                        new_by -= dy[i]
                    else:
                        new_rx -= dx[i]
                        new_ry -= dy[i]

                # (new_rx, new_ry), (new_bx, new_by) 를 동시에 방문한 적이 없다면
                if not visited[new_rx][new_ry][new_bx][new_by]:
                    visited[new_rx][new_ry][new_bx][new_by] = True
                    q.append((new_rx, new_ry, new_bx, new_by, cnt + 1))

    # 실패
    print(-1)


r_x, r_y = find('R')
b_x, b_y = find('B')


bfs(r_x, r_y, b_x, b_y)
