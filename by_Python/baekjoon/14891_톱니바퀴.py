import sys
from collections import deque
input = sys.stdin.readline

def rotate_gear(target, direction):
    if visited[target]:
        return
    
    # 현재 target 방문 표시
    visited[target] = True
    # 왼쪽 기어 확인
    if target - 1 >= 0:
        # 맞닿은 극이 다르면 반대방향으로 회전
        # target의 9시방향과 target-1의 3시방향 비교
        if gears[target][6] != gears[target-1][2]:
            rotate_gear(target-1, -direction)
    # 오른쪽 기어 확인
    if target + 1 < 4:
        if gears[target][2] != gears[target+1][6]:
            rotate_gear(target+1, -direction)
    
    # 현재 gear 회전
    gears[target].rotate(direction)

gears = [deque(list(input().strip())) for _ in range(4)]

for _ in range(int(input())):
    target, direction = map(int, input().split())
    target -= 1

    visited = [False]*4
    rotate_gear(target, direction)

# 점수 계산
score = 0
for i in range(4):
    score += int(gears[i][0]) * (2**i)
print(score)
