import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline


def dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def attack(game, archers, enemies):
    new_game = deepcopy(game)
    # 제거한 적 수를 구하기 위한 집합 (같은 적을 두번 죽였을 때 2로 카운트하지 않기 위해)
    # killed에 제거한 적의 좌표 (r, c)를 추가한다.
    killed = set()
    for archer in archers:
        targets = []  # 공격 가능한 적의 정보 저장 (거리, 행, 열)
        for enemy in enemies:
            r, c = enemy
            if dist(N, archer, r, c) <= D:
                targets.append((dist(N, archer, r, c), r, c))

        # 공격할 수 있는 적이 없는 경우
        if len(targets) == 0:
            continue

        # 현 archer가 공격할 적은 가장 가까운 적이고, 가장 왼쪽에 있는 적
        # 거리를 1순위, 열을 2순위로 targets를 정렬한다
        targets = sorted(targets, key=lambda x: (x[0], x[2]))
        # 최종 공격 적
        target = targets[0]
        new_game[target[1]][target[2]] = 0
        # 제거한 적 수 증가
        killed.add((target[1], target[2]))

    # 제거한 적 수와, 적을 제거한 뒤의 게임판 반환
    return len(killed), new_game


def get_enemies(arr):
    enemies = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                enemies.append((r, c))
    return enemies


N, M, D = map(int, input().split())
# 0 = 빈칸, 1 = 적
arr = [list(map(int, input().split())) for _ in range(N)] + [[0]*M]

# 궁수를 배치하는 경우의 수는 mC3
archer_combis = list(combinations(list(range(M)), 3))

# 궁수의 공격으로 제거할 수 있는 적의 최대 수
answer = 0

for archers in archer_combis:
    # 궁수를 archer 조합으로 배치한 경우의 게임 판
    game = deepcopy(arr)
    # 현 조합으로 궁수를 배치한 경우, 제거할 수 있는 적의 수
    total_cnt = 0
    # 적이 있는 위치 저장
    enemies = get_enemies(game)
    # 게임판 내에 적이 있을 때까지 게임 진행
    while enemies:
        cnt, new_game = attack(game, archers, enemies)
        total_cnt += cnt
        # 적 아래로 이동
        game = [[0]*M]
        for i in range(N-1):
            game += [new_game[i]]
        game += [[0]*M]
        # enemies 업데이트
        enemies = get_enemies(game)

    answer = max(answer, total_cnt)

print(answer)
