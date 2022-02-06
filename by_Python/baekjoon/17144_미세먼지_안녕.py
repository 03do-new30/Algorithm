import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]


def spread_dust(r, c, spread):  # 미세먼지 확산
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 확산된 방향의 개수
    cnt = 0

    # spread가 0이면 아래 과정 스킵
    if spread == 0:
        return

    for i in range(4):
        new_r = r + dx[i]
        new_c = c + dy[i]
        # 인접한 방향에 칸이 있는가?
        if 0 <= new_r < R and 0 <= new_c < C:
            # 인접한 방향에 공기청정기가 있는가?
            if A[new_r][new_c] > -1:
                A[new_r][new_c] += spread
                cnt += 1

    # (r, c)에 남은 미세먼지의 양
    A[r][c] -= spread * cnt


def purify(top_r, top_c, down_r, down_c):  # 공기청정기 작동
    # 위쪽 공기청정기 작동
    r_move = [0, -1, 0, 1]
    c_move = [1, 0, -1, 0]
    prev_dust = 0
    for i in range(4):
        while 0 <= top_r + r_move[i] < R and 0 <= top_c + c_move[i] < C:
            next_r = top_r + r_move[i]
            next_c = top_c + c_move[i]

            # 다음 칸이 공기청정기라면 끝
            if A[next_r][next_c] == -1:
                break

            cur_dust = A[next_r][next_c]
            A[next_r][next_c] = prev_dust

            # update
            prev_dust = cur_dust
            top_r = next_r
            top_c = next_c
    # 아래쪽 공기청정기 작동
    r_move = [0, 1, 0, -1]
    c_move = [1, 0, -1, 0]
    prev_dust = 0
    for i in range(4):
        while 0 <= down_r + r_move[i] < R and 0 <= down_c + c_move[i] < C:
            next_r = down_r + r_move[i]
            next_c = down_c + c_move[i]

            # 다음 칸이 공기청정기라면 끝
            if A[next_r][next_c] == -1:
                break

            cur_dust = A[next_r][next_c]
            A[next_r][next_c] = prev_dust

            # update
            prev_dust = cur_dust
            down_r = next_r
            down_c = next_c


# 공기청정기 좌표
machine = []
for r in range(R):
    for c in range(C):
        if A[r][c] == -1:
            machine.append((r, c))

# T초동안 실행
while T > 0:
    # 미세먼지 좌표와, 그 좌표에서 "확산시킬 미세먼지 양 "구하기
    dusts = []
    for r in range(R):
        for c in range(C):
            if A[r][c] > 0:
                spread = A[r][c] // 5
                dusts.append((r, c, spread))

    # 미세먼지가 있는 모든 칸에서 동시에 먼지 확산시키기
    for dust in dusts:
        dust_r, dust_c, dust_spread = dust
        spread_dust(dust_r, dust_c, dust_spread)

    """
    print('-'*30 + "먼지 확산")
    for row in A:
        print(row)
    """

    # 공기청정기 작동하기
    top = machine[0]
    down = machine[1]
    purify(top[0], top[1], down[0], down[1])

    """
    print('-'*30 + "공청기 작동")
    for row in A:
        print(row)
    """

    T -= 1

# 방에 남아있는 미세먼지의 양
ans = 0
for r in range(R):
    for c in range(C):
        if A[r][c] > 0:
            ans += A[r][c]
print(ans)
