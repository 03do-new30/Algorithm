# 출처: https://peisea0830.tistory.com/3
import sys
from unittest import result
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 땅을 고르는 데 걸리는 시간과 높이 저장
min_time = float('inf')
max_height = 0

# 기준이 되는 높이 h (0 <= h <= 256)
for h in range(257):
    # 초기 블록 + 인벤토리에 추가할 블록의 개수 >= 사용해야하는 블록의 개수 -> h로 땅을 고를 수 있음
    in_block = 0
    out_block = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] > h:
                in_block += arr[r][c] - h
            else:
                out_block += h - arr[r][c]
    
    inventory = in_block + B
    if inventory < out_block:
        continue

    time = in_block * 2 + out_block
    if time <= min_time:
        min_time = time
        # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
        # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
        # 시간이 같아도 최종적으로는ㄴ 높이가 높은 순으로 나오게 된다
        max_height = h
            

print(min_time, max_height)