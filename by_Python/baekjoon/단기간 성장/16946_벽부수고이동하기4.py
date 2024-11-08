import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# bfs
def bfs(r, c, visited, id):
    q = deque([(r, c)])
    visited[r][c] = id
    # 칸의 개수
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] > 0:
                    continue
                if arr[nr][nc] > 0:
                    continue
                visited[nr][nc] = id
                q.append((nr, nc))
    return cnt
    
# 매번 벽에서 탐색을 수행하면 시간이 너무 오래걸린다.

# 0(이동할 수 있는 곳)을 기준으로 잡자. 0끼리 영역을 이룬다고 생각하자.
# 각 영역마다 id를 매겨주고, 해당 id를 가진 영역에 0인 칸이 몇개 포함되는지 기록하자.
visited = [[0] * m for _ in range(n)]
id = 1 # 초기 id
parts = dict()
for r in range(n):
    for c in range(m):
        if arr[r][c] == 0 and visited[r][c] == 0:
            cnt = bfs(r, c, visited, id)
            parts[id] = cnt
            id += 1

# print("=== visited")
# for row in visited:
#     print(row)
# print("=== parts:", parts)

# 1(벽)인 칸을 순회하며, parts[인접한id]를 더해준다.
for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            # 인접한 구역의 id들을 기록하는 집합
            adj_ids = set()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if visited[nr][nc] == 0:
                        continue
                    adj_ids.add(visited[nr][nc])
            
            for adj_id in adj_ids:
                arr[r][c] += parts[adj_id]
                arr[r][c] %= 10

# print("=== 결과")
# for row in arr:
#     print(row)


for row in arr:
    print(''.join(list(map(str, row))))