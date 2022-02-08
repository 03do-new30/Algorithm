import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmd_list = list(map(int, input().split()))


def roll_dice(dice, dx, dy):
    new_dice = [[-1]*3 for _ in range(4)]
    # 남, 북으로 굴릴 때
    if dy == 0:
        # col = 1인 값들 수정
        # 남쪽으로 굴리는 경우
        if dx == 1:
            new_dice[0][1] = dice[-1][1]
            new_dice[1][1] = dice[0][1]
            new_dice[2][1] = dice[1][1]
            new_dice[3][1] = dice[2][1]
        # 북쪽으로 굴리는 경우
        else:
            new_dice[0][1] = dice[1][1]
            new_dice[1][1] = dice[2][1]
            new_dice[2][1] = dice[3][1]
            new_dice[3][1] = dice[0][1]
        # 좌, 우 유지
        new_dice[1][0] = dice[1][0]
        new_dice[1][2] = dice[1][2]
    # 동, 서로 굴릴 때
    else:
        # 서쪽으로 굴리는 경우
        if dy == -1:
            new_dice[1][0] = dice[1][1]
            new_dice[1][1] = dice[1][2]
            new_dice[1][2] = dice[3][1]
            new_dice[3][1] = dice[1][0]
        # 동쪽으로 굴리는 경우
        else:
            new_dice[1][0] = dice[3][1]
            new_dice[1][1] = dice[1][0]
            new_dice[1][2] = dice[1][1]
            new_dice[3][1] = dice[1][2]
        # 동, 서로 굴려도 유지되는 부분
        new_dice[0][1] = dice[0][1]
        new_dice[2][1] = dice[2][1]
    return new_dice


# 주사위의 전개도
# (1, 1)이 항상 상단의 숫자라고 본다
dice = [[-1]*3 for _ in range(4)]
dice[0][1] = dice[1][0] = dice[1][1] = dice[1][2] = dice[2][1] = dice[3][1] = 0

# 이동 방향
dirs = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

for cmd in cmd_list:

    dx = dirs[cmd][0]
    dy = dirs[cmd][1]

    # 이동한 칸의 좌표
    nx = x + dx
    ny = y + dy

    if 0 <= nx < N and 0 <= ny < M:
        # 주사위를 굴림
        dice = roll_dice(dice, dx, dy)
        """
        print('-'*30)
        for row in dice:
            print(row)
        """

        # 이동 칸에 쓰여있는 수가 0
        if arr[nx][ny] == 0:
            # 주사위의 바닥면에 쓰여있는 수가 칸에 복사
            arr[nx][ny] = dice[3][1]
        # 0이 아닌 경우
        else:
            # 칸에 쓰여있는 수가 주사위 바닥으로 복사
            dice[3][1] = arr[nx][ny]
            arr[nx][ny] = 0

        # x, y update
        x = nx
        y = ny

        # 주사위가 이동했을 때마다 상단에 쓰여 있는 값
        print(dice[1][1])
