import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def solve(a):
    virus = find_virus(a)
    bfs(a, virus)
    safety_zone = find_safety_zone(a)
    return safety_zone

def find_virus(a):
    ret = []
    for r in range(n):
        for c in range(m):
            if a[r][c] == 2:
                ret.append((r, c))
    return ret

def find_safety_zone(a):
    ret = 0
    for r in range(n):
        for c in range(m):
            if a[r][c] == 0:
                ret += 1
    return ret

def bfs(a, virus):
    q = deque(virus)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if a[nr][nc] == 0:
                    a[nr][nc] = 2
                    q.append((nr, nc))


answer = 0
for r1 in range(n):
    for c1 in range(m):
        if arr[r1][c1] != 0:
            continue
        for r2 in range(n):
            for c2 in range(m):
                if arr[r2][c2] != 0:
                    continue
                for r3 in range(n):
                    for c3 in range(m):
                        if arr[r3][c3] != 0:
                            continue
                        
                        if r1 == r2 and c1 == c2:
                            continue
                        if r1 == r3 and c1 == c3:
                            continue
                        if r2 == r3 and c2 == c3:
                            continue

                        arr[r1][c1] = 1; arr[r2][c2] = 1; arr[r3][c3] = 1
                        # solve
                        a = [row[:] for row in arr]
                        tmp = solve(a)
                        if answer < tmp:
                            answer = tmp
                        arr[r1][c1] = 0; arr[r2][c2] = 0;arr[r3][c3] = 0
print(answer)