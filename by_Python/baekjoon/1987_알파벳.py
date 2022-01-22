from copy import deepcopy
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
# 알파벳 대문자 -> 아스키 코드값 - 65로 바꾸어 저장
board = [list(map(lambda x: ord(x) - 65, list(input().strip())))
         for _ in range(r)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대 칸 수를 저장
max_ans = 0


def dfs(row, col, ans):

    global max_ans
    max_ans = max(max_ans, ans)

    for i in range(4):
        new_row = row + dx[i]
        new_col = col + dy[i]
        if 0 <= new_row < r and 0 <= new_col < c:
            if visited[board[new_row][new_col]] == 0:
                # 방문 처리
                visited[board[new_row][new_col]] = 1
                # dfs 수행
                dfs(new_row, new_col, ans + 1)
                # 방문 처리 해제
                visited[board[new_row][new_col]] = 0


visited = [0]*26
visited[board[0][0]] = 1
# 첫 칸 (0, 0)에서부터 탐색 시작
# 첫 칸도 칸 수에 포함되므로 ans = 1로 설정
dfs(0, 0, 1)
print(max_ans)
