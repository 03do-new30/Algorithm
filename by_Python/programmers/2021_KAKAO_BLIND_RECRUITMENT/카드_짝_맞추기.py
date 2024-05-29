# 참고: https://velog.io/@rltjr1092/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%EB%93%9C-%EC%A7%9D-%EB%A7%9E%EC%B6%94%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4

from collections import deque
INF = float('inf')
answer = INF

def get_key_count(board, start_r, start_c, target_r, target_c):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    q = deque([(start_r, start_c)])
    visited = [[INF] * 4 for _ in range(4)]
    visited[start_r][start_c] = 0

    while q:
        r, c = q.popleft()
        if r == target_r and c == target_c:
            return visited[target_r][target_c]
        # 방향키로만 이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if visited[nr][nc] > visited[r][c] + 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
        # ctrl 이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while 0 <= nr + dr[i] < 4 and 0 <= nc + dc[i] < 4 and board[nr][nc] == 0:
                nr += dr[i]
                nc += dc[i]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if visited[nr][nc] > visited[r][c] + 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
        
        
def get_card_loc(board, card):
    for i in range(4):
        for j in range(4):
            if board[i][j] == card:
                return i, j
    return -1, -1

def is_end(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                return False
    return True

# (start_r, start_c)에서 카드 번호가 board[r][c]인 쌍을 찾는다
def dfs(board, start_r, start_c, r1, c1, count):
    new_board = [row[:] for row in board]
    card = new_board[r1][c1]

    # (start_r, start_c) -> (r, c) 까지의 최소 키 횟수
    count += get_key_count(new_board, start_r, start_c, r1, c1)
    new_board[r1][c1] = 0

    # card의 다른 짝을 찾는다
    r2, c2 = get_card_loc(new_board, card)
    
    # (r, c) -> (r2, c2) 까지의 최소 키 횟수
    count += get_key_count(new_board, r1, c1, r2, c2)
    new_board[r2][c2] = 0 

    # 엔터키의 횟수를 더해준다
    count += 2

    if is_end(new_board):
        global answer

        answer = min(answer, count)
        return
    
    # 다음으로 뒤집을 카드를 찾는다
    for i in range(4):
        for j in range(4):
            if new_board[i][j] > 0:
                dfs(new_board, r2, c2, i, j, count)


def solution(board, r, c):
    global answer
    answer = INF
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                dfs(board, r, c, i, j, 0)
    # print("answer:", answer)
    return answer

board = [
    [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],
    [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],
    [[1,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]],
    [[0, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
]
r = [1, 0, 0, 0]
c = [0, 1, 0, 3]
result = [14, 16, 3, 5]
for i in range(4):
    print(solution(board[i], r[i], c[i]) == result[i])
    print('-' * 30)