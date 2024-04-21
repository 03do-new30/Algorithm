def solution(board, aloc, bloc):
    n = len(board); m = len(board[0])
    # DFS
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def movable(board, r, c):
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 1:
                    return True
        return False


    """
    이기는 사람은 최단경로로 이기려하고
    지는 사람은 최대경로로 진다
    재귀를 돌며 이길 수 있다면 최단경로를 반환하고
    질수밖에 없다면 최대경로를 반환한다
    """

    # turn_loc = 현재 움직일 차례인 사람의 좌표
    # other_loc = 상대의 좌표
    # return (성공 여부, 움직인 횟수)
    def move(board, turn_loc, other_loc):
        r, c = turn_loc
        # [1] 더이상 움직일 곳이 없으면 패배
        if not movable(board, r, c):
            return (False, 0)
        # [2] 서로 위치가 같을 때 먼저 움직인 사람이 이김
        if turn_loc == other_loc:
            return (True, 1)
        
        min_cnt = float('inf') # 현재 상태에서 움직이는 횟수 최소값 (무조건 승리하는 경우 이를 따른다)
        max_cnt = 0 # 현재 상태에서 움직이는 횟수 최대값 (무조건 패배하는 경우 이를 따른다)
        can_win = False # 현재 상태에서 이길 수 있는가?

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 1:
                    # 원래 위치 발판 삭제
                    board[r][c] = 0
                    # 다음 차례 진행
                    result = move(board, other_loc, (nr, nc))
                    # 백트래킹 (다음 차례 진행하면 other_loc 발판 빠질 가능성 있으므로 일단 1로 유지한다)
                    board[other_loc[0]][other_loc[1]] = 1

                    # result[0]이 False여야 이번 턴에서 내가 이길 수 있다
                    if not result[0]:
                        can_win = True
                        min_cnt = min(min_cnt, result[1])
                    else:
                        max_cnt = max(max_cnt, result[1])
        if can_win:
            cnt = min_cnt
        else:
            cnt = max_cnt
        return (can_win, cnt + 1)
        
    ret = move(board, aloc, bloc)
    answer = ret[1]
    return answer

board = [
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]	,
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]]	,
    [[1, 1, 1, 1, 1]]	,
    [[1]]	
]
aloc = [[1, 0], [1, 0], [0, 0], [0, 0]]
bloc = [[1, 2], [1, 2], [0, 4], [0, 0]]
result = [5, 4, 4, 0]
for i in range(len(result)):
    print(solution(board[i], aloc[i], bloc[i]) == result[i])
    print('-' * 30)