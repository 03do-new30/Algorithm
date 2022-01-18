from collections import deque
import sys
input = sys.stdin.readline

# 입력
n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 높이가 rain 이하인 모든 지점이 물이 잠겼을 때 안전 영역 계산


def count_safety(rain):
    count = 0
    visited = [[False]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if arr[row][col] > rain and not visited[row][col]:
                bfs(row, col, visited)
                count += 1

    return count


# bfs
def bfs(row, col, visited):
    q = deque([])
    q.append((row, col))

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        r, c = q.popleft()
        for move in moves:
            new_r = r + move[0]
            new_c = c + move[1]
            if 0 <= new_r < n and 0 <= new_c < n:
                # 높이가 rain보다 크면 안전영역에 포함
                # 방문 기록이 없어야 함
                if arr[new_r][new_c] > rain and not visited[new_r][new_c]:
                    q.append((new_r, new_c))
                    visited[new_r][new_c] = True


# 각 지역의 높이의 집합을 구하고,
# 내리는 비의 양이 그 원소일 때로 케이스를 나누어 안전영역 계산
rains = set()
for row in arr:
    for height in row:
        rains.add(height)
# 아무 지역도 물에 잠기지 않을 수도 있으므로, rains에 0을 추가
rains.add(0)

max_safety = 0
for rain in rains:
    max_safety = max(max_safety, count_safety(rain))

# 출력
print(max_safety)
