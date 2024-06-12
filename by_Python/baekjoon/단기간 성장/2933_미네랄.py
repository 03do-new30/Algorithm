import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
x = int(input())
sticks = list(map(int, input().split()))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r, c, cluster, id):
    q = deque([(r, c)])
    cluster[r][c] = id
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if cluster[nr][nc] == 0 and arr[nr][nc] == 'x':
                    cluster[nr][nc] = id
                    q.append((nr, nc))

def drop(cluster):
    # 클러스터 각 열의 맨 아래 부분 중 하나가 바닥 또는 미네랄 위로 떨어지는 입력만 주어진다
    result = [['.'] * m for _ in range(n)]

    col_minerals = dict()
    col_bottoms = dict() # 각 열의 맨 아래 부분들을 찾는다
    for r in range(n-1, -1, -1):
        for c in range(m):
            if cluster[r][c] < 2:
                result[r][c] = arr[r][c]
            else:
                # 2번 클러스터에 속하고
                if c in col_minerals:
                    col_minerals[c].append(r)
                else:
                    col_minerals[c] = [r]
                # 떠있는 미네랄인가?
                # 이미 저장되어있다면 패스
                if c in col_bottoms:
                    continue
                next_r = r + 1
                if next_r == n: # 바닥
                    continue
                if arr[next_r][c] == 'x': # 미네랄
                    continue # 떠있는 미네랄이 아님
                # 떠있는 미네랄이라면 col_bottoms에 저장
                col_bottoms[c] = r
            
    # print("col_minerals:", col_minerals)
    # print("col_bottoms:", col_bottoms)
    # 전체적으로 이동할 행
    global_row_cnt = n
    for col in col_bottoms:
        row = col_bottoms[col]
        next_row = row
        while next_row + 1 < n and arr[next_row +1][col] == '.':
            next_row += 1
        # 이동할 행
        row_cnt = next_row - row
        if row_cnt < global_row_cnt:
            global_row_cnt = row_cnt
    # 2번 클러스터에 있던 미네랄들 중 떠있던 미네랄들 -> 전체적으로 global_row_cnt만큼 이동시킨다
    # print("global_row_cnt:", global_row_cnt)
    for col in col_minerals:
        if col in col_bottoms: # 이동시킨다
            mineral_rows = col_minerals[col]
            for mineral_row in mineral_rows:
                result[mineral_row + global_row_cnt][col] = 'x'
        else: # 본인 자리 유지
            mineral_rows = col_minerals[col]
            for mineral_row in mineral_rows:
                result[mineral_row][col] = 'x'
    return result  

# i가 짝수이면 -> 방향으로 날아가고
# i가 홀수이면 <- 방향으로 날아간다.
for i in range(x):
    # print("----------", i+1, "번째 턴")
    r = n - sticks[i]
    crush_r = 0
    crush_c = 0
    if i % 2 == 0: # ->
        for c in range(m):
            if arr[r][c] == 'x':
                arr[r][c] = '.'
                break
    else:
        # <-
        for c in range(m-1, -1, -1):
            if arr[r][c] == 'x':
                arr[r][c] = '.'
                break
    # 클러스터 재정의
    cluster = [[0] * m for _ in range(n)]
    id = 1
    for i in range(n-1, -1, -1):
        for j in range(m):
            if cluster[i][j] == 0 and arr[i][j] == 'x':
                bfs(i, j, cluster, id)
                id += 1
    # 2번 클러스터가 있다면 2번 클러스터를 떨어뜨린다
    if id > 2:
        arr = drop(cluster)

for row in arr:
    print(''.join(row))