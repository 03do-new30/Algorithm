import sys
input = sys.stdin.readline

# n개의 강의, m개의 블루레이
n, m = map(int, input().split())
minutes = list(map(int, input().split()))

# 블루레이의 크기 중 최소를 구한다
left = max(minutes)
right = 1000000000

while left <= right:
    mid = (left + right) // 2
    # 한 블루레이의 크기가 mid일 때,
    # 총 몇개의 블루레이가 필요한지 저장한 변수 cnt
    cnt = 1
    tmp = 0
    for minute in minutes:
        if tmp + minute <= mid:
            tmp += minute
        else:
            tmp = minute
            cnt += 1
    
    # 필요한 블루레이의 개수가 할당된 개수 m을 초과하면
    if cnt > m:
        # 블루레이의 크기를 늘려야 한다
        left = mid + 1
    else:
        right = mid - 1

print(left)