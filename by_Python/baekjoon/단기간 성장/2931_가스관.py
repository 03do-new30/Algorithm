import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

# 0: 상, 1:하, 2: 좌, 3:우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# block_dirs['block'] = [상, 하, 좌, 우] 연결 가능 여부 1/0 표시
block_dirs = {'|':[1, 1, 0, 0],
          '-':[0, 0, 1, 1],
          '+':[1, 1, 1, 1],
          '1':[0, 1, 0, 1],
          '2':[1, 0, 0, 1],
          '3':[1, 0, 1, 0],
          '4':[0, 1, 1, 0],
          'M':[1, 1, 1, 1],
          'Z':[1, 1, 1, 1]}

def find_diconnection():
    mr = mc = -1
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 'M':
                mr = r
                mc = c
                break
    
    q = deque([(mr, mc)])
    visited = [[False] * m for _ in range(n)]
    visited[mr][mc] = True
    
    while q:
        r, c = q.popleft()
        dirs = block_dirs[arr[r][c]]
        for i in range(4):
            if not dirs[i]:
                continue
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc]:
                    continue
                # 파이프가 연결되어야 하는 칸이 빈칸이라면 disconnection
                if arr[nr][nc] == '.':
                    if arr[r][c] == 'M' or arr[r][c] == 'Z':
                        continue
                    else:
                        return (nr, nc)
                
                visited[nr][nc] = True
                q.append((nr, nc))
    return (-1, -1)

def get_valid_block(target_r, target_c):
    # (target_r, target_c)를 기준으로 상, 하, 좌, 우 블록들의 이동방향을 검사한다.
    # target: (target_r, target_c)의 [상, 하, 좌, 우] 연결 가능 여부
    target = [0, 0, 0, 0]
    for i in range(4):
        nr = target_r + dr[i]
        nc = target_c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] == '.':
                continue

            # 인접한 블록이 M이나 Z일때는 이 블록들과 연결되지 않도록 한다.
            # 그 이유는, M/Z가 하나의 블록과 이미 인접해 있는 입력만 주어지기 때문에 다시 M/Z로 가는 블록을 연결해줄 필요가 없음.
            if arr[nr][nc] == 'M' or arr[nr][nc] == 'Z':
                target[i] = 0
                continue

            # 위에 있는 블록의 '하' 방향 연결 여부를 target[0]('상' 방향 연결 여부)에 저장
            if i == 0:
                target[0] = block_dirs[arr[nr][nc]][1]
            # 아래에 있는 블록의 '상' 방향 연결 여부를 target[1]에 저장
            elif i == 1:
                target[1] = block_dirs[arr[nr][nc]][0]
            # 좌측에 있는 블록의 '우' 방향 연결 여부를 target[2]에 저장
            elif i == 2:
                target[2] = block_dirs[arr[nr][nc]][3]
            else:
                target[3] = block_dirs[arr[nr][nc]][2]         
    # 완성된 target에 알맞은 블록을 리턴한다.
    for block in block_dirs.keys():
        if block_dirs[block] == target:
            return block
    return '.'


# 연결이 끊기는 지점
target_r, target_c = find_diconnection()

# 연결이 끊기는 지점에 어떤 블록을 넣어야 파이프라인이 완성될지
answer = get_valid_block(target_r, target_c)

print(target_r + 1, target_c + 1, answer)