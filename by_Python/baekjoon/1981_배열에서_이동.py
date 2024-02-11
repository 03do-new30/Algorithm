import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def go(mid):
    # 지나는 수 중 가장 작은 수를 k라고 설정하자
    # 이때 최댓값과 최솟값의 차이가 mid가 될 수 있도록 지날 수 있는 수의 범위는 k ~ (k+mid)
    for k in range(200 - mid + 1):
        if bfs(k, mid):
            return True
    return False
    
# 배열에서 만나는 가장 작은 수의 값이 k일 때,
# 최댓값과 최솟값의 차이를 mid로 만들면서 (n, n)까지 도달 할 수 있는가
def bfs(k, mid):
    if k > arr[0][0] or arr[0][0] > k + mid:
        return False
    visited = [[False] * n for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and k <= arr[nr][nc] <= k + mid:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    
    return visited[n-1][n-1]
    
left = 0
right = 200
answer = 200

# 최댓값과 최솟값의 차이를 mid라고 할 때, (n, n)까지 도달 할 수 있는가?
while left <= right:
    mid = (left + right) // 2

    # 차이를 mid로 만들면서 (n, n)에 도달할 수 있었다면
    if go(mid):
        # 범위를 줄여본다
        right = mid - 1
        answer = min(mid, answer)
    else:
        left = mid + 1

print(answer)