from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 3차원 배열로 표현
# visited[r][c][0] -> 벽을 한 번도 안 뚫었을 때
# visited[r][c][1] -> 벽을 한번이라도 뚫었을 때
visited = [[[0] * 2 for _ in range(m)] for __ in range(n)]

# flag가 1일 때 -> 벽을 한 번이라도 뚫음
# flag가 0일 때 -> 벽을 한 번도 안 뚫음


def bfs(r, c, flag):
    q = deque([])
    q.append((r, c, flag))
    visited[r][c][flag] = 1

    while q:

        r, c, flag = q.popleft()

        """
        if flag == 0:
            print("벽을 파괴하지 않은", end=' ')
        else:
            print("벽을 파괴한", end=' ')
        print("(", r, ",", c, ")", "에서 탐색한 결과")
        """

        for i in range(4):
            new_r = r + dx[i]
            new_c = c + dy[i]

            if 0 <= new_r < n and 0 <= new_c < m:
                if arr[new_r][new_c] == 0:
                    if visited[new_r][new_c][flag] == 0:
                        visited[new_r][new_c][flag] = visited[r][c][flag] + 1
                        q.append((new_r, new_c, flag))
                else:
                    if flag == 0:
                        # print("(", new_r, ",", new_c, ") 에서 벽을 파괴")
                        visited[new_r][new_c][1] = visited[r][c][0] + 1
                        q.append((new_r, new_c, 1))
        """
        for row in visited:
            print(row)
        print('='*20)
        """


# bfs 실행
bfs(0, 0, 0)

# 출력
if 0 in visited[n-1][m-1]:
    min_dist = max(visited[n-1][m-1][0], visited[n-1][m-1][1])
else:
    min_dist = min(visited[n-1][m-1][0], visited[n-1][m-1][1])

if min_dist == 0:
    print(-1)
else:
    print(min_dist)
