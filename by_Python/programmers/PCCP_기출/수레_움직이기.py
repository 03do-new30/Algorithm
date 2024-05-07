def solution(maze):
    # 1: 빨간 수레의 시작 칸 -> 3: 도착
    # 2: 파란 수레의 시작 칸 -> 4: 도착
    # 5: 벽
    n = len(maze); m = len(maze[0])

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    
    rr = -1; rc = -1; br = -1; bc = -1
    for r in range(n):
        for c in range(m):
            if maze[r][c] == 1:
                rr = r
                rc = c
            elif maze[r][c] == 2:
                br = r
                bc = c
    # 벽
    def is_wall(r, c):
        return maze[r][c] == 5
    
    # 격자판 밖
    def is_inbound(r, c):
        return 0 <= r < n and 0 <= c < m
    
    # 수레끼리 자리를 바꾸며 움직였는지
    def is_changed(rr, rc, new_rr, new_rc, br, bc, new_br, new_bc):
        if rr == new_br and rc == new_bc\
            and br == new_rr and bc == new_rc:
            return True
        return False
    
    r_check = [[False] * m for _ in range(n)]
    b_check = [[False] * m for _ in range(n)]
    r_check[rr][rc] = True
    b_check[br][bc] = True

    got_answer = False
    answer = float('inf')

    def dfs(rr, rc, br, bc, cnt):
        nonlocal answer, got_answer

        # print("rr:", rr, "rc:", rc, "br:", br, "bc:", bc, "cnt:", cnt)
        # print("r_check")
        # for row in r_check:
        #     print(row)
        # print("b_check")
        # for row in b_check:
        #     print(row)
        # print('@-' * 20)
        if maze[rr][rc] == 3 and maze[br][bc] == 4:
            r_arrived = True
            b_arrived = True
        else:
            if maze[rr][rc] == 3:
                r_arrived = True
                b_arrived = False
            elif maze[br][bc] == 4:
                r_arrived = False
                b_arrived = True
            else:
                r_arrived = False
                b_arrived = False

        if r_arrived and b_arrived:
            got_answer = True
            if cnt < answer:
                answer = cnt
            # 현재 턴수가 구한 answer보다 크다면 더이상 탐색할 필요 없다
            if cnt > answer:
                return
        
        if not r_arrived and not b_arrived:
            for i in range(4):
                new_rr = rr + dr[i]
                new_rc = rc + dc[i]

                if not is_inbound(new_rr, new_rc):
                    continue
                if is_wall(new_rr, new_rc):
                    continue
                if r_check[new_rr][new_rc]:
                    if not r_arrived:
                        continue
                
                for j in range(4):
                    new_br = br + dr[j]
                    new_bc = bc + dc[j]
                    if not is_inbound(new_br, new_bc):
                        continue
                    if is_wall(new_br, new_bc):
                        continue
                    if b_check[new_br][new_bc]:
                        if not b_arrived:
                            continue
                    
                    # (new_rr, new_rc), (new_br, new_bc) 이동 가능한 경우
                    if new_rr == new_br and new_rc == new_bc:
                        continue
                    if is_changed(rr, rc, new_rr, new_rc, br, bc, new_br, new_bc):
                        continue
                    r_check[new_rr][new_rc] = True
                    b_check[new_br][new_bc] = True
                    dfs(new_rr, new_rc, new_br, new_bc, cnt + 1)
                    r_check[new_rr][new_rc] = False
                    b_check[new_br][new_bc] = False
            
        elif r_arrived and not b_arrived:
            for j in range(4):
                new_br = br + dr[j]
                new_bc = bc + dc[j]
                if not is_inbound(new_br, new_bc):
                    continue
                if is_wall(new_br, new_bc):
                    continue
                if b_check[new_br][new_bc]:
                    if not b_arrived:
                        continue
                
                # (rr, rc), (new_br, new_bc) 이동 가능한 경우
                if rr == new_br and rc == new_bc:
                    continue
                b_check[new_br][new_bc] = True
                dfs(rr, rc, new_br, new_bc, cnt + 1)
                b_check[new_br][new_bc] = False
        elif b_arrived and not r_arrived:
            for i in range(4):
                new_rr = rr + dr[i]
                new_rc = rc + dc[i]
                if not is_inbound(new_rr, new_rc):
                    continue
                if is_wall(new_rr, new_rc):
                    continue
                if r_check[new_rr][new_rc]:
                    if not r_arrived:
                        continue
                
                # (new_rr, new_rc), (br, bc) 이동 가능한 경우
                if new_rr == br and new_rc == bc:
                    continue
                r_check[new_rr][new_rc] = True
                dfs(new_rr, new_rc, br, bc, cnt + 1)
                r_check[new_rr][new_rc] = False
    dfs(rr, rc, br, bc, 0)
    if got_answer:
        return answer
    else:
        return 0

maze = [
    [[1, 4], [0, 0], [2, 3]]	,
    [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]	,
    [[1, 5], [2, 5], [4, 5], [3, 5]]	,
    [[4, 1, 2, 3]],
    [[4, 3, 0, 0], [5, 5, 5, 0], [1, 0, 0, 0], [2, 0, 0, 0]]
]
result = [3, 7, 0, 0, 9]
for i in range(len(result)):
    print(solution(maze[i]) == result[i])
    print('-' * 30)