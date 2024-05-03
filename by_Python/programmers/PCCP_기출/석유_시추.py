from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    visited = [[0] * m for _ in range(n)]
    oil_size = dict()

    def bfs(r, c, oil_id):
        q = deque([(r, c)])
        visited[r][c] = oil_id
        cnt = 0
        while q:
            r, c = q.popleft()
            cnt += 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if land[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] = oil_id
                        q.append((nr, nc)) 
        oil_size[oil_id] = cnt
    
    oil_id = 1
    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and visited[r][c] == 0:
                bfs(r, c, oil_id)
                oil_id += 1

    answer = 0
    for c in range(m):
        oil_ids = set()
        for r in range(n):
            if visited[r][c] != 0:
                oil_ids.add(visited[r][c])
        tmp = 0
        for id in oil_ids:
            tmp += oil_size[id]
        if tmp > answer:
            answer = tmp
            

    return answer
    


land = [
    [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]	,
    [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]	
]
result = [9, 16]
for i in range(len(result)):
    print(solution(land[i]) == result[i])