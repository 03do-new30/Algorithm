import sys
input = sys.stdin.readline
from collections import deque

def num_to_row_col(n):
    # n번 칸 -> 몇번째 행, 몇번째 열에 위치하는지 리턴
    if n % 10 == 0:
        row = n // 10 - 1
        col = 9
    else:
        row = n // 10
        col = (n % 10) - 1
    return row, col

def row_col_to_num(r, c):
    if c == 9:
        return (r+1)*10
    
    return r*10 + (c+1)

def bfs():
    q = deque([(0, 0, 0)])
    visited = [[False]*10 for _ in range(10)]
    visited[0][0] = True

    while q:
        r, c, cnt = q.popleft()
        num = row_col_to_num(r, c)

        if num == 100:
            return cnt

        for i in range(1, 7):
            new_num = num + i
            
            if new_num > 100:
                break
            
            new_r, new_c = num_to_row_col(new_num)

            if not visited[new_r][new_c]:
                if board[new_r][new_c] == 0:
                    q.append((new_r, new_c, cnt + 1))
                    visited[new_r][new_c] = True
                else:
                    # 뱀이나 사다리 칸일 때

                    # 다른 뱀이나 사다리칸을 만나지 않을 때까지 반복한다
                    while board[new_r][new_c] != 0:
                        # new_r, new_c 방문 표시!
                        visited[new_r][new_c] = True
                        # 이동해야하는 move_r, move_c
                        move_r, move_c = board[new_r][new_c]
                        # 업데이트
                        new_r, new_c = move_r, move_c
                    
                    # 마지막으로 도달한 칸을 q에 추가해준다
                    q.append((new_r, new_c, cnt + 1))

board = [[0]*10 for _ in range(10)]
N, M = map(int, input().split())
# 사다리
for _ in range(N):
    x, y = map(int, input().split())
    x_row, x_col = num_to_row_col(x)
    y_row, y_col = num_to_row_col(y)
    board[x_row][x_col] = (y_row, y_col)
# 뱀
for _ in range(M):
    u, v = map(int, input().split())
    u_row, u_col = num_to_row_col(u)
    v_row, v_col = num_to_row_col(v)
    board[u_row][u_col] = (v_row, v_col)

ans = bfs()
print(ans)