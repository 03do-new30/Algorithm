import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_arr = min(map(min, arr))
max_arr = max(map(max, arr))
max_diff = max_arr - min_arr

def bfs(min_val, max_val):
    # min_val 이상, max_val 이하의 값을 지나며
    # (n-1, n-1)까지 도달할 수 있는가?
    if arr[0][0] < min_val or arr[0][0] > max_val:
        return False
    
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    q = deque([(0, 0)])

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while q:
        r, c = q.popleft()
        if r == n-1 and c == n-1:
            return True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not(0 <= nr < n and 0 <= nc < n):
                continue
            if arr[nr][nc] < min_val or arr[nr][nc] > max_val:
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
    
    return False

def solve(goal):
    # 차이를 goal로 만들면서 (0, 0)에서 (n-1, n-1)까지 도달할 수 있는가?

    # 차이를 goal로 만들 때, 지날 수 있는 최소값은 min_val이고 최대값은 min_val + goal이다.
    for min_val in range(min_arr, max_arr + 1):
        max_val = min_val + goal
        if max_val > max_arr:
            break
        if bfs(min_val, max_val):
            return True
    return False

left = 0
right = max_diff
answer = max_diff
# 이분탐색
while left <= right:
    mid = (left + right) // 2
    success = solve(mid)
    if success:
        answer = min(answer, mid)
        # 차이를 mid로 만드는 데 성공했다면, 차이를 더 줄여볼 수 있다.
        right = mid - 1
    else:
        left = mid + 1

print(answer)