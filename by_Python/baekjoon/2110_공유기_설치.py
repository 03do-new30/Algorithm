import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left = 1
right = arr[-1] # 인접한 거리의 최대

while left <= right:
    mid = (left + right) // 2
    # mid가 가장 인접한 두 공유기 사이의 거리일 때
    # 공유기를 몇개 설치할 수 있는가?
    cnt = 0
    prev = -1
    for x in arr:
        if prev == -1:
            prev = x
            cnt += 1
            continue
        if prev + mid <= x:
            prev = x
            cnt += 1
    # print("cnt:", cnt)
    # 가장 인접한 두 공유기 사이의 거리를 mid로 설정했을 떄
    # 공유기를 설치할 수 있는 개수는 cnt개
    # cnt >= c 이면 가장 인접한 두 공유기 사이의 거리를 더 크게 해본다
    if cnt >= c:
        left = mid + 1
    else:
        right = mid - 1

print(right)
