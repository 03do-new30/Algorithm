import sys
input = sys.stdin.readline
from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 0-1 BFS
def bfs(r, c):
    q = deque([(r, c)])
    visited = [[-1] * (m+2) for _ in range(n+2)]
    visited[r][c] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n+2 and 0 <= nc < m+2:
                if visited[nr][nc] != -1:
                    continue
                if arr[nr][nc] == '*':
                    continue
                if arr[nr][nc] == '.' or arr[nr][nc] == '$':
                    # 큐의 앞에 넣어준다
                    q.appendleft((nr, nc))
                    visited[nr][nc] = visited[r][c]
                elif arr[nr][nc] == '#':
                    # 큐의 뒤에 넣어준다
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
        
    return visited

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [['.'] * (m+2)] + [['.'] + list(input().strip()) + ['.'] for _ in range(n)] + [['.'] * (m+2)]
    # 죄수들의 위치를 찾아 저장
    prisoners = []
    for r in range(1, n+1):
        for c in range(1, m+1):
            if arr[r][c] == '$':
                prisoners.append((r, c))

    # 죄수 1, 죄수 2가 탈출하는 경우와 외부에서 죄수1, 죄수2를 만나러 오는 경우로 나누어 생각한다
    # 세 경우 구한 벽을 부수는 횟수의 최소값을 구한다
    
    # 죄수 1이 탈출하는 경우
    visited_1 = bfs(prisoners[0][0], prisoners[0][1])
    # 죄수 2가 탈출하는 경우
    visited_2 = bfs(prisoners[1][0], prisoners[1][1])
    # 외부에서 죄수 1, 2를 만나러 오는 경우
    visited_3 = bfs(0, 0)
    
    # 세 결과를 합쳐본다
    answer = float('inf')
    for r in range(1, n+1):
        for c in range(1, m+1):
            
            if visited_1[r][c] != -1 and visited_2[r][c] != -1 and visited_3[r][c] != -1:
                res = visited_1[r][c] + visited_2[r][c] + visited_3[r][c]
                
                if arr[r][c] == '*':
                    continue
                if arr[r][c] == '#':
                    # 셋 다 해당 벽을 부순 거니까 -2 해준다
                    res -= 2 
                answer = min(answer, res)
                
    print(answer)
    
    
    
    