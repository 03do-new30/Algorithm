import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

def solve(arr):
    ans = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    flag = 1
    flag_counts = dict()
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0 and visited[r][c] == 0:
                flag_count = bfs(r, c, visited, flag)
                flag_counts[flag] = flag_count
                flag += 1
    
    # visited로 벽에 인접해있는 빈칸의 flag들을 확인하고
    # flag_counts에서 각 flag별 빈칸 개수를 구한다
    # 어떤 벽 (r, c)를 부수고 갈 수 있는 칸의 개수는
    # 1 + 인접한 flag_counts들 값
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                tmp = 1
                flags = set()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < n and 0 <= nc < m:
                        if visited[nr][nc] != 0:
                            flags.add(visited[nr][nc])
                for f in flags:
                    tmp += flag_counts[f]
                ans[r][c] = tmp % 10
                        
    return ans

def bfs(r, c, visited, flag):
    # (r, c)에서 이동할 수 있는 칸의 개수를 세어본다
    q = deque([(r, c)])
    visited[r][c] = flag
    ret = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = flag
                    q.append((nr, nc))
                    ret += 1
    return ret

ans = solve(arr)
for row in ans:
    print(''.join(list(map(str, row))))