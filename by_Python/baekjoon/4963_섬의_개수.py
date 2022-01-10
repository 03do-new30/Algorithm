import sys
from collections import deque
input = sys.stdin.readline


def island(row, col, arr):
    q = deque([])
    q.append((row, col))
    arr[row][col] = -1  # if visited -> -1

    moves = [[-1, 0], [1, 0], [0, -1], [0, 1],
             [-1, -1], [-1, 1], [1, 1], [1, -1]]

    while q:
        r, c = q.popleft()
        for move in moves:
            new_r = r + move[0]
            new_c = c + move[1]
            if 0 <= new_r < h and 0 <= new_c < w:
                if arr[new_r][new_c] == 1:
                    q.append((new_r, new_c))
                    arr[new_r][new_c] = -1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    count = 0
    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1:
                island(r, c, arr)
                count += 1

    print(count)
