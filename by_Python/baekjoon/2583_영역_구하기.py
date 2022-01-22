from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

# 상하좌우로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상하 반전된 그림이 나오지만, 빈 영역을 구하는 데 영향을 주진 않음


def draw(x1, y1, x2, y2):
    for r in range(y1, y2):
        for c in range(x1, x2):
            # 직사각형의 내부는 1로 표시
            arr[r][c] = 1


def bfs(row, col):
    q = deque([])
    q.append((row, col))
    arr[row][col] = -1
    # 영역의 넓이
    size = 1

    while q:
        row, col = q.popleft()
        for i in range(4):
            new_row = row + dx[i]
            new_col = col + dy[i]

            if 0 <= new_row < m and 0 <= new_col < n:
                if arr[new_row][new_col] == 0:
                    # 방문 표시 = -1
                    arr[new_row][new_col] = -1
                    q.append((new_row, new_col))
                    size += 1

    return size


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    draw(x1, y1, x2, y2)

# 영역의 개수
cnt = 0
# 각 영역의 넓이를 오름차순으로 정렬
sizes = []
for row in range(m):
    for col in range(n):
        if arr[row][col] == 0:
            sizes.append(bfs(row, col))
            cnt += 1

print(cnt)
sizes = sorted(sizes)
for x in sizes:
    print(x, end=' ')
print()
