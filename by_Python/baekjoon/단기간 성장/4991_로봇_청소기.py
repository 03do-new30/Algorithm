import sys
input = sys.stdin.readline

from collections import deque
from itertools import permutations

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# (r, c)에서 모든 지점에 대해 BFS
def bfs(arr, r, c):
    n = len(arr)
    m = len(arr[0])

    q = deque([(r, c)])
    dist = [[-1] * m for _ in range(n)]
    dist[r][c] = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 'x':
                    continue
                if dist[nr][nc] > -1:
                    continue
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    
    return dist

# dist를 통해 방문할 수 없는 지점이 있는지 확인한다.
def exists_non_reachable_point(arr, dist):
    n = len(arr)
    m = len(arr[0])
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 'x':
                continue
            if dist[r][c] == -1:
                return True
    return False

while True:
    m, n = map(int, input().split())
    
    if m == 0 and n == 0:
        break

    arr = [list(input().strip()) for _ in range(n)]


    # 로봇 청소기의 시작 위치를 찾는다
    start_r = -1
    start_c = -1
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 'o':
                start_r = r
                start_c = c
                break
    
    # 출발점을 포함해 각 지점에서 각각 BFS를 하여 다른 지점들까지 가는 최단거리를 구한다.
    # 탐색해야 할 지점: 출발점 + 더러운 칸
    points = [(start_r, start_c)]
    for r in range(n):
        for c in range(m):
            if arr[r][c] == '*':
                points.append((r, c))
    
    # min_dist[i][j] = points[i] - points[j]의 최단거리
    INF = float('inf')
    min_dist = [[INF] * len(points) for _ in range(len(points))]
    

    # 최단거리를 저장할 변수
    answer = INF

    for i in range(len(points)-1):
        # dist: points[i]에서 전 지점으로의 최단거리를 구한 결과
        i_row, i_col = points[i]
        dist = bfs(arr, i_row, i_col)

        # 방문할 수 없는 지점이 있는 경우
        if exists_non_reachable_point(arr, dist):
            answer = -1
            break

        for j in range(i+1, len(points)):
            if i == j:
                min_dist[i][j] = 0
            
            j_row, j_col = points[j]
            min_dist[i][j] = min_dist[j][i] = dist[j_row][j_col]
    
    """
    print("===== min_dist =====")
    for row in min_dist:
       print(row)
    """
    
    # 도달할 수 없는 지점이 있다면 -1 출력
    if answer == -1:
        print(answer)
    else:
        # points[0](시작점)을 제외하고 나머지 지점들로 순열을 만든다.
        # 이후, 각각의 케이스에서 모든 칸을 청소할 때까지 걸리는 거리를 구하고, 그 중 최소를 구한다.
        orders = list(permutations(range(1, len(points)), len(points) - 1))
        
        for order in orders:
            tmp_dist = 0
            for i in range(len(order)):
                if i == 0:
                    # 시작점에서 order[i]번째 더러운 칸까지의 거리를 구한다.
                    tmp_dist += min_dist[0][order[i]]
                else:
                    # order[i-1]번째 더러운 칸에서 order[i]번째 더러운 칸까지의 거리를 구한다.
                    tmp_dist += min_dist[order[i-1]][order[i]]
            
            if answer > tmp_dist:
                answer = tmp_dist
        print(answer)