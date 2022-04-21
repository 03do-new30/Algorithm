import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

# 이분 탐색
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    # mid 길이로 잘랐을 때 나오는 랜선 개수
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    
    if cnt < N:
        # 좀 더 작게 잘라서 개수를 늘려야 한다
        end = mid - 1
    else:
        # 개수가 N보다 많으면 더 크게 잘라도 된다
        start = mid + 1

print(end)