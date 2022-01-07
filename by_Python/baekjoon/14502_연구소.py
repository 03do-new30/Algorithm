import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

"""
참고: https://mentha2.tistory.com/24
"""


def bfs(row, col, arr):
    # lab[row][col] == 2
    queue = deque([])
    queue.append((row, col))

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        v = queue.popleft()
        for move in moves:
            new_row = v[0] + move[0]
            new_col = v[1] + move[1]
            if 0 <= new_row < n and 0 <= new_col < m:
                if arr[new_row][new_col] == 0:  # empty
                    queue.append((new_row, new_col))
                    arr[new_row][new_col] = 2  # virus


# save safety set
safety_set = set()


def wall(arr):
    # save empty area
    empty_list = []
    for r in range(n):
        for c in range(m):
            if lab[r][c] == 0:
                empty_list.append((r, c))

    # make combinations of empty area = possible walls
    wall_combinations = list(combinations(empty_list, 3))

    # build wall for each combination
    for combi in wall_combinations:
        new_arr = [arr_row[:] for arr_row in arr]
        new_arr[combi[0][0]][combi[0][1]] = 1  # wall
        new_arr[combi[1][0]][combi[1][1]] = 1  # wall
        new_arr[combi[2][0]][combi[2][1]] = 1  # wall

        # bfs
        for r in range(n):
            for c in range(m):
                if new_arr[r][c] == 2:
                    bfs(r, c, new_arr)

        # update max_safety
        safety_set.add(safety_area(new_arr))


def safety_area(arr):
    result = 0
    for row in arr:
        result += row.count(0)
    return result


wall(lab)
print(max(safety_set))
