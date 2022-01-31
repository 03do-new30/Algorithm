import sys
from collections import deque
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(8)]

# 찐 구현으로 푼 방법
# 0, 2, 4, ... 짝수 row의 짝수 col -> 흰색
# 1, 3, 5, ... 홀수 row의 홀수 col -> 흰색
count = 0
for row in range(8):
    for col in range(8):
        if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
            if board[row][col] == 'F':
                count += 1
print(count)

# bfs로 풀수도 있음
""" 
same_color_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
visited = [[False]*8 for _ in range(8)]


def bfs(row, col):
    count = 0
    if board[row][col] == 'F':
        count += 1
    q = deque([(row, col)])
    visited[row][col] = True
    while q:
        row, col = q.popleft()
        for move in same_color_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if not visited[new_row][new_col]:
                    if board[new_row][new_col] == 'F':
                        count += 1
                    visited[new_row][new_col] = True
                    q.append((new_row, new_col))
    return count


print(bfs(0, 0))
"""
